# Client Application JavaScript Engine for MAKAUT Semester V Platform
def get_js():
    return """
const DATA = window.DATA;
// Global Application State & Storage Controllers
const AppStore = {
  getCompletedTopics() {
    try { return JSON.parse(localStorage.getItem('makaut_completed_topics') || '[]'); } catch { return []; }
  },
  toggleCompletedTopic(id) {
    let completed = this.getCompletedTopics();
    if (completed.includes(id)) {
      completed = completed.filter(t => t !== id);
    } else {
      completed.push(id);
    }
    localStorage.setItem('makaut_completed_topics', JSON.stringify(completed));
    AppRouter.updateProgressPill();
    return completed.includes(id);
  },
  getBookmarks() {
    try { return JSON.parse(localStorage.getItem('makaut_bookmarks') || '[]'); } catch { return []; }
  },
  toggleBookmark(id) {
    let bookmarks = this.getBookmarks();
    if (bookmarks.includes(id)) {
      bookmarks = bookmarks.filter(b => b !== id);
    } else {
      bookmarks.push(id);
    }
    localStorage.setItem('makaut_bookmarks', JSON.stringify(bookmarks));
    return bookmarks.includes(id);
  },
  getPreparedExams() {
    try { return JSON.parse(localStorage.getItem('makaut_prepared_exams') || '[]'); } catch { return []; }
  },
  togglePreparedExam(id) {
    let prepared = this.getPreparedExams();
    if (prepared.includes(id)) {
      prepared = prepared.filter(e => e !== id);
    } else {
      prepared.push(id);
    }
    localStorage.setItem('makaut_prepared_exams', JSON.stringify(prepared));
    return prepared.includes(id);
  },
  getLastTopic() {
    return localStorage.getItem('makaut_last_topic') || 'php_m1_t1';
  },
  setLastTopic(id) {
    localStorage.setItem('makaut_last_topic', id);
  },
  resetAll() {
    if (confirm("Are you sure you want to reset all your learning progress, bookmarks, and prepared questions?")) {
      localStorage.removeItem('makaut_completed_topics');
      localStorage.removeItem('makaut_bookmarks');
      localStorage.removeItem('makaut_prepared_exams');
      localStorage.removeItem('makaut_last_topic');
      AppRouter.updateProgressPill();
      AppRouter.navigate(window.location.hash || '#home');
    }
  }
};

// Router and View Engine
const AppRouter = {
  init() {
    window.addEventListener('hashchange', () => this.handleRoute());
    this.updateProgressPill();
    this.initSearch();
    this.handleRoute();
  },

  updateProgressPill() {
    const completed = AppStore.getCompletedTopics();
    const totalTopics = this.getTotalTopicCount();
    const pct = totalTopics > 0 ? Math.round((completed.length / totalTopics) * 100) : 0;
    const pill = document.getElementById('global-progress-pill');
    if (pill) {
      pill.innerHTML = `<span>⚡ Progress:</span> <strong>${pct}%</strong> (${completed.length}/${totalTopics})`;
    }
  },

  getTotalTopicCount() {
    let count = 0;
    DATA.curriculum.subjects.forEach(s => {
      s.modules.forEach(m => {
        count += (m.topics || []).length;
      });
    });
    return count;
  },

  navigate(hash) {
    window.location.hash = hash;
  },

  handleRoute() {
    const rawHash = window.location.hash || '#home';
    const parts = rawHash.replace('#', '').split('/');
    const route = parts[0] || 'home';
    const param = parts[1];

    // Update active nav links
    document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.bottom-nav-item').forEach(el => el.classList.remove('active'));

    const navId = 'nav-' + (route === '' ? 'home' : route);
    const navEl = document.getElementById(navId);
    if (navEl) navEl.classList.add('active');

    const bNavId = 'bnav-' + (route === '' ? 'home' : route);
    const bNavEl = document.getElementById(bNavId);
    if (bNavEl) bNavEl.classList.add('active');

    const container = document.getElementById('page-container');
    if (!container) return;

    window.scrollTo({ top: 0, behavior: 'smooth' });

    if (route === 'home') {
      this.renderHome(container);
    } else if (route === 'curriculum') {
      this.renderCurriculum(container);
    } else if (route === 'subject') {
      this.renderSubject(container, param);
    } else if (route === 'topic') {
      this.renderTopic(container, param);
    } else if (route === 'exams') {
      this.renderExams(container, param);
    } else if (route === 'practicals') {
      this.renderPracticals(container, param);
    } else if (route === 'quiz') {
      this.renderQuiz(container);
    } else if (route === 'bookmarks') {
      this.renderBookmarks(container);
    } else {
      this.renderHome(container);
    }
  },

  // 1. HOME DASHBOARD
  renderHome(container) {
    const completed = AppStore.getCompletedTopics();
    const totalTopics = this.getTotalTopicCount();
    const progressPct = totalTopics > 0 ? Math.round((completed.length / totalTopics) * 100) : 0;
    const lastTopicId = AppStore.getLastTopic();
    const lastTopic = this.findTopic(lastTopicId);

    let subjectsHtml = '';
    DATA.curriculum.subjects.forEach(s => {
      let subjTopics = 0;
      let subjCompleted = 0;
      s.modules.forEach(m => {
        (m.topics || []).forEach(t => {
          subjTopics++;
          if (completed.includes(t.id)) subjCompleted++;
        });
      });
      const sPct = subjTopics > 0 ? Math.round((subjCompleted / subjTopics) * 100) : 0;

      subjectsHtml += `
        <div class="subject-card">
          <div class="subject-card-header">
            <span class="subject-code">${s.code}</span>
            <span class="subject-credits">${s.credits} Credits • ${s.total_hours}h</span>
          </div>
          <h3 class="subject-name">${s.name}</h3>
          <p class="subject-desc">${s.objective || 'Complete syllabus curriculum extracted from university regulations.'}</p>
          <div class="subject-meta-chips">
            <span class="meta-chip">${s.category}</span>
            <span class="meta-chip">${s.modules.length} Modules</span>
            <span class="meta-chip">${s.total_marks} Marks</span>
          </div>
          <div class="card-progress-bar">
            <div class="card-progress-fill" style="width: ${sPct}%;"></div>
          </div>
          <div style="display:flex; justify-content:space-between; align-items:center; margin-top:auto;">
            <span style="font-size:12px; color:var(--text-secondary); font-weight:600;">${subjCompleted}/${subjTopics} Topics</span>
            <a href="#subject/${s.id}" class="btn-primary" style="padding:6px 14px; font-size:12px;">Explore Syllabus →</a>
          </div>
        </div>
      `;
    });

    container.innerHTML = `
      <div class="hero-card">
        <div class="hero-tag">🎓 Maulana Abul Kalam Azad University of Technology (MAKAUT)</div>
        <h1 class="hero-title">Academic Digital Learning Platform</h1>
        <p class="hero-subtitle">BCA & MIM • Semester V (2023-24 Session) • Dynamic Syllabus Curriculum, Model Examination Answers, Practical Labs, and Interactive Assessment.</p>
        
        <div style="background:#fff; border-radius:var(--radius-sm); border:1px solid var(--border-color); padding:16px; margin-bottom:20px; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:12px;">
          <div>
            <div style="font-size:11px; text-transform:uppercase; font-weight:700; color:var(--text-secondary); margin-bottom:4px;">📌 Continue Learning</div>
            <div style="font-size:15px; font-weight:700; color:var(--text-primary);">${lastTopic ? lastTopic.title : 'Introduction to Web Development'}</div>
            <div style="font-size:12px; color:var(--text-secondary);">${lastTopic ? lastTopic.subject_name + ' • Module ' + lastTopic.module_no : 'PHP WITH MYSQL'}</div>
          </div>
          <a href="#topic/${lastTopicId}" class="btn-primary">Resume Topic →</a>
        </div>

        <div class="stats-grid">
          <div class="stat-box">
            <span class="stat-num">${DATA.curriculum.subjects.length}</span>
            <span class="stat-label">Theory Subjects</span>
          </div>
          <div class="stat-box">
            <span class="stat-num">${totalTopics}</span>
            <span class="stat-label">Detailed Lessons</span>
          </div>
          <div class="stat-box">
            <span class="stat-num">${DATA.flat_exams.length}</span>
            <span class="stat-label">Model Exam Q&As</span>
          </div>
          <div class="stat-box">
            <span class="stat-num">${DATA.practicals.bcac591.length + DATA.practicals.bcac592.length}</span>
            <span class="stat-label">Practical Lab Cases</span>
          </div>
          <div class="stat-box">
            <span class="stat-num">${DATA.quizzes.length}</span>
            <span class="stat-label">Quiz Bank Items</span>
          </div>
        </div>
      </div>

      <div class="section-header">
        <h2 class="section-title">📚 Prescribed Semester V Curriculum</h2>
        <span style="font-size:13px; color:var(--text-secondary); font-weight:600;">Overall Progress: ${progressPct}%</span>
      </div>

      <div class="subject-grid">
        ${subjectsHtml}
      </div>

      <div class="section-header">
        <h2 class="section-title">🧪 Prescribed Practical Laboratory Papers</h2>
      </div>

      <div class="subject-grid">
        <div class="subject-card">
          <div class="subject-card-header">
            <span class="subject-code">BCAC591</span>
            <span class="subject-credits">2 Credits • 6 Cases</span>
          </div>
          <h3 class="subject-name">PHP WITH MYSQL LAB</h3>
          <p class="subject-desc">Comprehensive lab curriculum featuring 6 prescribed projects: User Authentication, CMS, Voting System, Catalog, Event Manager, and Forum.</p>
          <div style="margin-top:auto;">
            <a href="#practicals/bcac591" class="btn-outline" style="width:100%;">View 6 Lab Cases →</a>
          </div>
        </div>
        <div class="subject-card">
          <div class="subject-card-header">
            <span class="subject-code">BCAC592</span>
            <span class="subject-credits">2 Credits • 6 Cases</span>
          </div>
          <h3 class="subject-name">Java OOP Laboratory</h3>
          <p class="subject-desc">Implementation of 6 core case studies: Library System, Corporate Payroll, Thread-safe Banking, Vehicle Rental, Inventory Serialization, and Hotel Booking.</p>
          <div style="margin-top:auto;">
            <a href="#practicals/bcac592" class="btn-outline" style="width:100%;">View 6 Lab Cases →</a>
          </div>
        </div>
      </div>
    `;
  },

  // 2. CURRICULUM OVERVIEW (SECTION A)
  renderCurriculum(container) {
    let content = `
      <div class="section-header">
        <h1 class="section-title">📖 Section A: Topic-wise Syllabus Learning</h1>
        <button class="btn-secondary-sm" onclick="window.print()">🖨️ Print Curriculum</button>
      </div>
      <p style="font-size:14px; color:var(--text-secondary); margin-bottom:24px;">Explore detailed 8-part topic lessons for all active subjects extracted from university regulations.</p>
    `;

    DATA.curriculum.subjects.forEach(s => {
      content += `
        <div style="background:#fff; border:1px solid var(--border-color); border-radius:var(--radius-md); padding:24px; margin-bottom:24px; box-shadow:var(--shadow-sm);">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; border-bottom:1px solid var(--border-color); padding-bottom:12px;">
            <div>
              <span class="subject-code">${s.code}</span>
              <h2 style="font-size:18px; font-weight:700; color:var(--text-primary); margin-top:6px;">${s.name}</h2>
            </div>
            <a href="#subject/${s.id}" class="btn-primary" style="padding:6px 14px; font-size:12px;">Subject View →</a>
          </div>
          <div style="display:flex; flex-direction:column; gap:12px;">
      `;

      s.modules.forEach(m => {
        content += `
          <div style="background:var(--bg-page); padding:12px 16px; border-radius:var(--radius-sm);">
            <div style="font-size:13px; font-weight:700; color:var(--text-primary); margin-bottom:6px;">Module ${m.module_no}: ${m.title} <span style="font-size:11px; font-weight:500; color:var(--text-secondary);">(${m.hours || 6} Hours)</span></div>
            <div style="display:flex; flex-wrap:wrap; gap:8px;">
        `;
        (m.topics || []).forEach(t => {
          const isDone = AppStore.getCompletedTopics().includes(t.id);
          content += `
            <a href="#topic/${t.id}" style="font-size:12px; text-decoration:none; color:${isDone ? 'var(--success)' : 'var(--vibrant-blue)'}; background:#fff; border:1px solid ${isDone ? '#BBF7D0' : 'var(--border-color)'}; padding:4px 10px; border-radius:6px; font-weight:500;">
              ${isDone ? '✓ ' : ''}${t.title}
            </a>
          `;
        });
        content += `</div></div>`;
      });

      content += `</div></div>`;
    });

    container.innerHTML = content;
  },

  // 3. SUBJECT MODULES VIEW
  renderSubject(container, subjectId) {
    const s = DATA.curriculum.subjects.find(sub => sub.id === subjectId) || DATA.curriculum.subjects[0];
    const completed = AppStore.getCompletedTopics();

    let modulesHtml = '';
    s.modules.forEach(m => {
      let topicsList = '';
      (m.topics || []).forEach(t => {
        const isDone = completed.includes(t.id);
        const isBookmarked = AppStore.getBookmarks().includes(t.id);
        topicsList += `
          <div style="display:flex; align-items:center; justify-content:space-between; padding:12px 16px; border-bottom:1px solid var(--border-color); background:#fff;">
            <div style="display:flex; align-items:center; gap:12px;">
              <span style="color:${isDone ? 'var(--success)' : '#cbd5e1'}; font-size:16px;">${isDone ? '●' : '○'}</span>
              <div>
                <a href="#topic/${t.id}" style="font-size:14px; font-weight:600; color:var(--text-primary); text-decoration:none;">${t.title}</a>
                <div style="font-size:11px; color:var(--text-secondary);">${(t.subtopics || []).slice(0, 3).join(' • ')}</div>
              </div>
            </div>
            <div style="display:flex; align-items:center; gap:10px;">
              ${isBookmarked ? '<span style="font-size:12px; color:var(--yellow);" title="Bookmarked">★</span>' : ''}
              <a href="#topic/${t.id}" class="btn-outline" style="padding:4px 10px; font-size:12px;">Study Lesson →</a>
            </div>
          </div>
        `;
      });

      modulesHtml += `
        <div style="background:#fff; border:1px solid var(--border-color); border-radius:var(--radius-md); margin-bottom:20px; overflow:hidden; box-shadow:var(--shadow-sm);">
          <div style="background:var(--bg-page); padding:14px 20px; border-bottom:1px solid var(--border-color); display:flex; justify-content:space-between; align-items:center;">
            <h3 style="font-size:15px; font-weight:700; color:var(--text-primary);">Module ${m.module_no}: ${m.title}</h3>
            <span style="font-size:12px; color:var(--text-secondary); font-weight:600;">${m.hours || 6} Teaching Hours</span>
          </div>
          <div>${topicsList}</div>
        </div>
      `;
    });

    container.innerHTML = `
      <div style="margin-bottom:24px;">
        <div class="lesson-breadcrumbs">
          <a href="#home">Home</a> &gt; <a href="#curriculum">Curriculum</a> &gt; <span>${s.code}</span>
        </div>
        <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:16px;">
          <div>
            <span class="subject-code">${s.code}</span>
            <h1 style="font-size:24px; font-weight:800; color:var(--text-primary); margin-top:8px;">${s.name}</h1>
            <p style="font-size:14px; color:var(--text-secondary); margin-top:4px;">${s.category} • ${s.credits} Credits • ${s.total_hours} Total Hours • ${s.total_marks} Marks</p>
          </div>
          <div style="display:flex; gap:10px;">
            <a href="#exams/${s.id}" class="btn-outline">Exam Questions (${s.code})</a>
            <a href="#quiz?subject=${s.id}" class="btn-primary">Take Subject Quiz</a>
          </div>
        </div>
      </div>

      <div>${modulesHtml}</div>
    `;
  },

  // 4. TOPIC LESSON VIEW (Mandatory 8-Part Structure)
  renderTopic(container, topicId) {
    const topicInfo = this.findTopic(topicId);
    if (!topicInfo) {
      container.innerHTML = `<div class="hero-card"><h2>Topic Not Found</h2><p>The requested topic could not be located.</p><a href="#home" class="btn-primary">Return Home</a></div>`;
      return;
    }

    AppStore.setLastTopic(topicId);
    const t = topicInfo.topic;
    const isCompleted = AppStore.getCompletedTopics().includes(topicId);
    const isBookmarked = AppStore.getBookmarks().includes(topicId);

    // Build Terminology Cards
    let termHtml = '';
    (t.fundamentals.terminology || []).forEach(term => {
      termHtml += `
        <div class="term-card">
          <div class="term-name">${term.term}</div>
          <div class="term-def">${term.definition}</div>
        </div>
      `;
    });

    // Build Comparison Table
    let tableHtml = '';
    if (t.detailed_explanation.comparison_table && t.detailed_explanation.comparison_table.headers) {
      const headers = t.detailed_explanation.comparison_table.headers.map(h => `<th>${h}</th>`).join('');
      const rows = t.detailed_explanation.comparison_table.rows.map(r => `<tr>${r.map(c => `<td>${c}</td>`).join('')}</tr>`).join('');
      tableHtml = `
        <div class="data-table-wrapper">
          <table class="data-table">
            <thead><tr>${headers}</tr></thead>
            <tbody>${rows}</tbody>
          </table>
        </div>
      `;
    }

    // Next / Previous Navigation links
    const prevTopic = topicInfo.prev;
    const nextTopic = topicInfo.next;

    container.innerHTML = `
      <div class="lesson-container">
        <!-- Breadcrumbs & Header -->
        <div class="lesson-header">
          <div class="lesson-breadcrumbs">
            <a href="#home">Home</a> &gt; <a href="#subject/${topicInfo.subject_id}">${topicInfo.subject_code}</a> &gt; <span>Module ${topicInfo.module_no}</span>
          </div>
          <h1 class="lesson-title">${t.title}</h1>
          <div class="lesson-subtopics">
            ${(t.subtopics || []).map(st => `<span class="subtopic-pill">${st}</span>`).join('')}
          </div>
        </div>

        <!-- Part 1: Introduction -->
        <div class="lesson-section">
          <h2 class="lesson-section-title"><span class="part-badge">Part 1</span> Introduction &amp; Scientific Background</h2>
          <div class="prose">
            <p><strong>Definition:</strong> ${t.intro.definition}</p>
            <p><strong>Scientific Background:</strong> ${t.intro.background}</p>
            <p><strong>Academic Importance:</strong> ${t.intro.importance}</p>
            <div style="background:var(--bg-page); padding:14px 18px; border-radius:var(--radius-sm); border-left:3px solid var(--vibrant-blue);">
              <strong style="color:var(--text-primary); font-size:13px;">Learning Objectives:</strong>
              <ul style="margin-top:6px; margin-bottom:0;">
                ${(t.intro.objectives || []).map(ob => `<li>${ob}</li>`).join('')}
              </ul>
            </div>
          </div>
        </div>

        <!-- Part 2: Fundamental Understanding -->
        <div class="lesson-section">
          <h2 class="lesson-section-title"><span class="part-badge">Part 2</span> Fundamental Concepts &amp; Core Terminology</h2>
          <div class="prose">
            <p>${t.fundamentals.concepts}</p>
            <div class="term-grid">
              ${termHtml}
            </div>
            <div class="alert-box alert-tip" style="margin-top:16px;">
              <div>💡</div>
              <div><strong>Core Scientific Principles:</strong><br>${t.fundamentals.principles}</div>
            </div>
          </div>
        </div>

        <!-- Part 3: Detailed Explanation -->
        <div class="lesson-section">
          <h2 class="lesson-section-title"><span class="part-badge">Part 3</span> Detailed Sequential Explanation &amp; Mechanism</h2>
          <div class="prose">
            <ol>
              ${(t.detailed_explanation.sequence || []).map(sq => `<li>${sq}</li>`).join('')}
            </ol>
            ${tableHtml}
            ${t.detailed_explanation.code_architecture ? `
              <div class="code-container">
                <div class="code-header">
                  <span>Architecture / Syntax Blueprint</span>
                  <button class="btn-copy" onclick="navigator.clipboard.writeText(this.dataset.code)" data-code="${this.escapeHtml(t.detailed_explanation.code_architecture)}">Copy</button>
                </div>
                <pre class="code-pre"><code>${this.escapeHtml(t.detailed_explanation.code_architecture)}</code></pre>
              </div>
            ` : ''}
          </div>
        </div>

        <!-- Part 4: Scientific Diagrams -->
        <div class="lesson-section">
          <h2 class="lesson-section-title"><span class="part-badge">Part 4</span> Labelled Scientific Architecture Diagram</h2>
          <div class="diagram-container">
            ${t.diagram.svg}
            <div class="diagram-caption">${t.diagram.caption}</div>
          </div>
        </div>

        <!-- Part 5: Relevant Examples -->
        <div class="lesson-section">
          <h2 class="lesson-section-title"><span class="part-badge">Part 5</span> Practical Implementation &amp; Production Example</h2>
          <div class="prose">
            <p><strong>Scenario:</strong> ${t.examples.scenario}</p>
            <div class="code-container">
              <div class="code-header">
                <span>Working Implementation</span>
                <button class="btn-copy" onclick="navigator.clipboard.writeText(this.dataset.code)" data-code="${this.escapeHtml(t.examples.code)}">Copy Code</button>
              </div>
              <pre class="code-pre"><code>${this.escapeHtml(t.examples.code)}</code></pre>
            </div>
          </div>
        </div>

        <!-- Part 6: Important Points (5-8 Revision Points) -->
        <div class="lesson-section">
          <h2 class="lesson-section-title"><span class="part-badge">Part 6</span> Key Examination Revision Points</h2>
          <div style="background:#fff; border:1px solid #E5E9F1; border-radius:var(--radius-sm); padding:16px;">
            <ul style="margin-left:20px;">
              ${(t.important_points || []).map(pt => `<li style="margin-bottom:8px; font-size:14px; color:var(--text-primary);">${pt}</li>`).join('')}
            </ul>
          </div>
        </div>

        <!-- Part 7: Quick Revision -->
        <div class="lesson-section">
          <h2 class="lesson-section-title"><span class="part-badge">Part 7</span> Quick Revision &amp; Common Pitfalls</h2>
          <div style="background:var(--bg-page); border-radius:var(--radius-sm); padding:18px;">
            <p style="margin-bottom:10px;"><strong>Topic Summary:</strong> ${t.revision.summary}</p>
            <p style="margin-bottom:10px;"><strong>Key Terms:</strong> <code>${t.revision.terminology}</code></p>
            <p style="margin-bottom:10px;"><strong>Major Mechanism:</strong> ${t.revision.mechanisms}</p>
            <div class="alert-box alert-warning" style="margin-top:12px; margin-bottom:0;">
              <div>⚠️</div>
              <div><strong>Common Conceptual Mistakes to Avoid:</strong><br>${t.revision.common_mistakes}</div>
            </div>
          </div>
        </div>

        <!-- Part 8: Learning Actions Bar -->
        <div class="actions-bar">
          <div style="display:flex; gap:10px; align-items:center;">
            <button class="btn-outline" id="btn-toggle-complete" onclick="AppRouter.toggleComplete('${t.id}')">
              ${isCompleted ? '✓ Completed' : '○ Mark as Completed'}
            </button>
            <button class="btn-outline" id="btn-toggle-bookmark" onclick="AppRouter.toggleBookmark('${t.id}')">
              ${isBookmarked ? '★ Bookmarked' : '☆ Bookmark Topic'}
            </button>
          </div>
          <div class="action-buttons-group">
            ${prevTopic ? `<a href="#topic/${prevTopic.id}" class="btn-outline">← Prev Topic</a>` : ''}
            ${nextTopic ? `<a href="#topic/${nextTopic.id}" class="btn-primary">Next Topic →</a>` : ''}
            <a href="#exams/${topicInfo.subject_id}" class="btn-outline">Exam Q&amp;As</a>
            <a href="#quiz?subject=${topicInfo.subject_id}&unit=${topicInfo.module_no}" class="btn-primary">Take Topic Quiz</a>
          </div>
        </div>
      </div>
    `;
  },

  toggleComplete(id) {
    const isNowDone = AppStore.toggleCompletedTopic(id);
    const btn = document.getElementById('btn-toggle-complete');
    if (btn) btn.innerHTML = isNowDone ? '✓ Completed' : '○ Mark as Completed';
  },

  toggleBookmark(id) {
    const isNowBookmarked = AppStore.toggleBookmark(id);
    const btn = document.getElementById('btn-toggle-bookmark');
    if (btn) btn.innerHTML = isNowBookmarked ? '★ Bookmarked' : '☆ Bookmark Topic';
  },

  // 5. SECTION B: MODEL EXAMINATION QUESTIONS (Mandatory 4-Part Structure)
  renderExams(container, filterSubj) {
    const activeSubj = filterSubj || 'all';
    const preparedList = AppStore.getPreparedExams();

    let filteredExams = DATA.flat_exams;
    if (activeSubj !== 'all') {
      filteredExams = DATA.flat_exams.filter(e => e.subject_id === activeSubj);
    }

    let filterPills = `
      <a href="#exams" class="meta-chip ${activeSubj === 'all' ? 'active' : ''}" style="text-decoration:none; padding:6px 14px; font-weight:600; ${activeSubj === 'all' ? 'background:var(--vibrant-blue); color:#fff;' : ''}">All Subjects (40 Q&amp;As)</a>
    `;
    DATA.curriculum.subjects.forEach(s => {
      const isAct = activeSubj === s.id;
      filterPills += `
        <a href="#exams/${s.id}" class="meta-chip" style="text-decoration:none; padding:6px 14px; font-weight:600; ${isAct ? 'background:var(--vibrant-blue); color:#fff;' : ''}">
          ${s.code} (10 Qs)
        </a>
      `;
    });

    let cardsHtml = '';
    filteredExams.forEach(e => {
      const isPrepared = preparedList.includes(e.id);
      cardsHtml += `
        <div class="exam-card" id="${e.id}">
          <div class="exam-card-header">
            <span class="exam-q-num">Q${e.question_no} • ${e.subject_id.toUpperCase()}</span>
            <h3 class="exam-q-title">${e.title}</h3>
            <div style="display:flex; align-items:center; gap:8px;">
              <button class="btn-outline" style="padding:4px 8px; font-size:11px;" onclick="AppRouter.togglePrepared('${e.id}')">
                ${isPrepared ? '✓ Prepared' : 'Mark Prepared'}
              </button>
            </div>
          </div>

          <!-- 1. INTRODUCTION -->
          <div style="margin-bottom:18px;">
            <div class="exam-part-label">1. Introduction &amp; Scientific Background</div>
            <p style="font-size:14px; color:var(--text-primary); margin-bottom:6px;"><strong>Definition:</strong> ${e.intro.definition}</p>
            <p style="font-size:13px; color:var(--text-secondary); margin-bottom:6px;"><strong>Background:</strong> ${e.intro.background}</p>
            <p style="font-size:13px; color:var(--text-secondary);"><strong>Significance:</strong> ${e.intro.significance}</p>
          </div>

          <!-- 2. DIAGRAM -->
          <div style="margin-bottom:20px;">
            <div class="exam-part-label">2. Labelled Scientific Diagram</div>
            <div class="diagram-container" style="padding:14px; margin:10px 0;">
              ${e.diagram.svg}
              <div class="diagram-caption">${e.diagram.caption}</div>
            </div>
            <p style="font-size:13px; color:var(--text-secondary);">${e.diagram.explanation}</p>
          </div>

          <!-- 3. FIVE MAIN POINTS -->
          <div style="margin-bottom:18px;">
            <div class="exam-part-label">3. Five Main University Examination Points</div>
            ${e.points.map(pt => `
              <div class="exam-point-item">
                <div class="exam-point-heading">${pt.point_no}. ${pt.heading}</div>
                <div class="exam-point-desc">${pt.explanation}</div>
                <div class="exam-point-meta">
                  <strong>Terminology:</strong> ${pt.terminology} | <strong>Example:</strong> <code>${pt.example}</code>
                </div>
              </div>
            `).join('')}
          </div>

          <!-- 4. CONCLUSION -->
          <div style="background:var(--bg-page); border-radius:var(--radius-sm); padding:14px;">
            <div class="exam-part-label">4. Academic Conclusion</div>
            <p style="font-size:13px; color:var(--text-primary); line-height:1.5;">${e.conclusion}</p>
          </div>
        </div>
      `;
    });

    container.innerHTML = `
      <div style="margin-bottom:24px;">
        <h1 class="section-title">📝 Section B: Model Examination Questions &amp; Answers</h1>
        <p style="font-size:14px; color:var(--text-secondary); margin-top:4px;">Exactly 10 comprehensive model questions per theory subject (40 Q&amp;As) strictly adhering to the 4-part structure.</p>
        <div style="display:flex; flex-wrap:wrap; gap:8px; margin-top:16px;">
          ${filterPills}
        </div>
      </div>

      <div>${cardsHtml}</div>
    `;
  },

  togglePrepared(id) {
    AppStore.togglePreparedExam(id);
    const hash = window.location.hash || '#exams';
    this.handleRoute();
  },

  // 6. SECTION D: PRACTICAL LABS VIEW
  renderPracticals(container, activeLabParam) {
    const activeLab = activeLabParam || 'bcac591';
    const cases = DATA.practicals[activeLab] || DATA.practicals.bcac591;

    let casesHtml = '';
    cases.forEach(c => {
      casesHtml += `
        <div class="exam-card" style="margin-bottom:28px;">
          <div class="exam-card-header">
            <span class="exam-q-num">Lab Case ${c.case_no}</span>
            <h3 class="exam-q-title">${c.title}</h3>
            <span class="meta-chip">${c.code}</span>
          </div>

          <div style="margin-bottom:16px;">
            <p style="font-size:14px; color:var(--text-primary); margin-bottom:6px;"><strong>Objective:</strong> ${c.objective}</p>
            <p style="font-size:13px; color:var(--text-secondary); margin-bottom:6px;"><strong>Scientific Principle:</strong> ${c.principle}</p>
            <p style="font-size:13px; color:var(--text-secondary);"><strong>Materials &amp; Setup:</strong> ${c.materials_setup}</p>
          </div>

          <div style="margin-bottom:16px;">
            <div class="exam-part-label">Architectural Flowchart</div>
            <div class="diagram-container" style="padding:14px; margin:8px 0;">
              ${c.architecture_svg}
            </div>
          </div>

          <div style="margin-bottom:16px;">
            <div class="exam-part-label">Step-by-Step Procedure</div>
            <ul style="margin-left:20px; font-size:13px; color:var(--text-secondary);">
              ${c.procedure_steps.map(s => `<li style="margin-bottom:4px;">${s}</li>`).join('')}
            </ul>
          </div>

          <div style="margin-bottom:16px;">
            <div class="exam-part-label">Complete Production Source Code</div>
            <div class="code-container">
              <div class="code-header">
                <span>Executable Implementation</span>
                <button class="btn-copy" onclick="navigator.clipboard.writeText(this.dataset.code)" data-code="${this.escapeHtml(c.full_code)}">Copy Full Code</button>
              </div>
              <pre class="code-pre"><code>${this.escapeHtml(c.full_code)}</code></pre>
            </div>
          </div>

          <div style="margin-bottom:16px;">
            <div class="exam-part-label">Expected Outputs &amp; Verification</div>
            <div style="background:var(--bg-page); padding:12px 14px; border-radius:var(--radius-sm); font-size:13px; font-family:var(--font-mono); color:var(--text-primary);">
              ${(c.expected_outputs || '').split(String.fromCharCode(10)).join('<br>')}
            </div>
            <p style="font-size:13px; color:var(--text-secondary); margin-top:8px;"><strong>Interpretation:</strong> ${c.interpretation}</p>
          </div>

          <div>
            <div class="exam-part-label">Lab Viva Voce Questions &amp; Detailed Answers</div>
            ${c.viva_qa.map(v => `
              <div class="viva-box">
                <div class="viva-q">Q: ${v.q}</div>
                <div class="viva-a">A: ${v.a}</div>
              </div>
            `).join('')}
          </div>
        </div>
      `;
    });

    container.innerHTML = `
      <div style="margin-bottom:24px;">
        <h1 class="section-title">🧪 Section D: Practical Laboratory Case Studies</h1>
        <p style="font-size:14px; color:var(--text-secondary); margin-top:4px;">Prescribed laboratory case studies complete with objectives, source code, outputs, and viva voce preparation.</p>
        <div style="display:flex; gap:12px; margin-top:16px;">
          <a href="#practicals/bcac591" class="btn-outline ${activeLab === 'bcac591' ? 'btn-primary' : ''}" style="${activeLab === 'bcac591' ? 'background:var(--vibrant-blue); color:#fff;' : ''}">
            BCAC591: PHP with MySQL Lab (6 Cases)
          </a>
          <a href="#practicals/bcac592" class="btn-outline ${activeLab === 'bcac592' ? 'btn-primary' : ''}" style="${activeLab === 'bcac592' ? 'background:var(--vibrant-blue); color:#fff;' : ''}">
            BCAC592: Java OOP Lab (6 Cases)
          </a>
        </div>
      </div>

      <div>${casesHtml}</div>
    `;
  },

  // 7. SECTION C: INTERACTIVE QUIZ ENGINE
  renderQuiz(container) {
    container.innerHTML = `
      <div class="quiz-config-card">
        <h1 class="section-title">🎯 Section C: Interactive Knowledge Assessment</h1>
        <p style="font-size:14px; color:var(--text-secondary); margin-top:4px;">Filterable academic quiz engine covering Single MCQ, Multi-select, True/False, and Case Applications.</p>
        
        <div class="filter-row">
          <div class="form-group">
            <label>Subject</label>
            <select class="form-select" id="quiz-filter-subject">
              <option value="all">All Subjects (84 Questions)</option>
              <option value="bcac501">BCAC501: PHP with MySQL</option>
              <option value="bcac502">BCAC502: Java OOP</option>
              <option value="mim502">MIM 502: Entrepreneurship</option>
              <option value="mim501">MIM501: Financial Management</option>
            </select>
          </div>
          <div class="form-group">
            <label>Difficulty Tier</label>
            <select class="form-select" id="quiz-filter-diff">
              <option value="all">All Difficulties</option>
              <option value="easy">Easy (Fundamentals)</option>
              <option value="medium">Medium (Analytical)</option>
              <option value="hard">Hard (Advanced / Case Study)</option>
            </select>
          </div>
          <div class="form-group">
            <label>Question Count</label>
            <select class="form-select" id="quiz-filter-count">
              <option value="10">10 Questions</option>
              <option value="15">15 Questions</option>
              <option value="20">20 Questions</option>
              <option value="all">All Matching Questions</option>
            </select>
          </div>
        </div>

        <div style="margin-top:20px; display:flex; justify-content:flex-end;">
          <button class="btn-primary" onclick="AppRouter.startAssessment()">Start Assessment Test →</button>
        </div>
      </div>

      <div id="quiz-active-area"></div>
    `;
  },

  startAssessment() {
    const subj = document.getElementById('quiz-filter-subject').value;
    const diff = document.getElementById('quiz-filter-diff').value;
    const countVal = document.getElementById('quiz-filter-count').value;

    let pool = [...DATA.quizzes];
    if (subj !== 'all') pool = pool.filter(q => q.subject_id === subj);
    if (diff !== 'all') pool = pool.filter(q => q.difficulty === diff);

    // Shuffle
    pool.sort(() => Math.random() - 0.5);

    let count = pool.length;
    if (countVal !== 'all') {
      count = Math.min(parseInt(countVal), pool.length);
    }
    const selected = pool.slice(0, count);

    const target = document.getElementById('quiz-active-area');
    if (!target) return;

    if (selected.length === 0) {
      target.innerHTML = `<div class="hero-card"><p>No questions matched the selected filters. Please broaden your selection.</p></div>`;
      return;
    }

    window._activeQuizQuestions = selected;
    window._quizSelections = {};
    window._quizSubmitted = false;

    let itemsHtml = '';
    selected.forEach((q, idx) => {
      itemsHtml += `
        <div class="quiz-card" id="qcard-${q.id}">
          <div class="quiz-meta-row">
            <span>Question ${idx + 1} of ${selected.length} • ${q.subject_id.toUpperCase()}</span>
            <span class="meta-chip">${q.difficulty.toUpperCase()} • ${q.type.replace('_', ' ').toUpperCase()}</span>
          </div>
          <div class="quiz-question-text">${q.question}</div>
          <div class="options-list">
            ${q.options.map((opt, optIdx) => `
              <div class="option-item" id="opt-${q.id}-${optIdx}" onclick="AppRouter.selectQuizOption('${q.id}', ${optIdx}, '${q.type}')">
                <span style="font-weight:700; color:var(--text-secondary); width:20px;">${String.fromCharCode(65 + optIdx)}.</span>
                <span style="flex:1;">${opt}</span>
              </div>
            `).join('')}
          </div>
          <div class="explanation-card" id="exp-${q.id}" style="display:none;"></div>
        </div>
      `;
    });

    target.innerHTML = `
      <div style="margin-bottom:20px; display:flex; justify-content:space-between; align-items:center; background:#fff; padding:16px 20px; border-radius:var(--radius-sm); border:1px solid var(--border-color);">
        <span style="font-weight:700; color:var(--text-primary);">Test in Progress (${selected.length} questions)</span>
        <button class="btn-primary" id="btn-submit-quiz" onclick="AppRouter.submitAssessment()">Submit Assessment</button>
      </div>
      <div>${itemsHtml}</div>
    `;
  },

  selectQuizOption(qId, optIdx, type) {
    if (window._quizSubmitted) return;

    if (!window._quizSelections[qId]) {
      window._quizSelections[qId] = [];
    }

    if (type === 'multi_mcq') {
      const idx = window._quizSelections[qId].indexOf(optIdx);
      if (idx > -1) {
        window._quizSelections[qId].splice(idx, 1);
        document.getElementById(`opt-${qId}-${optIdx}`).classList.remove('selected');
      } else {
        window._quizSelections[qId].push(optIdx);
        document.getElementById(`opt-${qId}-${optIdx}`).classList.add('selected');
      }
    } else {
      // Single or True/False
      window._quizSelections[qId] = [optIdx];
      const q = window._activeQuizQuestions.find(item => item.id === qId);
      if (q) {
        q.options.forEach((_, i) => {
          const el = document.getElementById(`opt-${qId}-${i}`);
          if (el) el.classList.remove('selected');
        });
      }
      document.getElementById(`opt-${qId}-${optIdx}`).classList.add('selected');
    }
  },

  submitAssessment() {
    if (window._quizSubmitted) return;
    window._quizSubmitted = true;

    const questions = window._activeQuizQuestions || [];
    let correctCount = 0;

    questions.forEach(q => {
      const userSelected = window._quizSelections[q.id] || [];
      const correctIndices = q.correct_indices;

      const isExactMatch = userSelected.length === correctIndices.length &&
        userSelected.every(idx => correctIndices.includes(idx));

      if (isExactMatch) correctCount++;

      // Highlight options
      q.options.forEach((_, i) => {
        const optEl = document.getElementById(`opt-${q.id}-${i}`);
        if (!optEl) return;
        optEl.classList.remove('selected');
        if (correctIndices.includes(i)) {
          optEl.classList.add('correct');
        } else if (userSelected.includes(i)) {
          optEl.classList.add('incorrect');
        }
      });

      // Show explanation
      const expEl = document.getElementById(`exp-${q.id}`);
      if (expEl) {
        expEl.style.display = 'block';
        expEl.innerHTML = `
          <strong>${isExactMatch ? '✓ Correct Answer!' : '✗ Incorrect'}</strong><br>
          ${q.explanation}
        `;
      }
    });

    const scorePct = Math.round((correctCount / questions.length) * 100);
    const submitBtn = document.getElementById('btn-submit-quiz');
    if (submitBtn) {
      submitBtn.style.display = 'none';
    }

    const target = document.getElementById('quiz-active-area');
    if (target) {
      const reportHtml = `
        <div class="hero-card" style="margin-bottom:24px; background:linear-gradient(135deg, #F0FDF4 0%, #FFFFFF 100%); border-color:#BBF7D0;">
          <h2 style="font-size:22px; font-weight:800; color:#166534; margin-bottom:6px;">Assessment Complete!</h2>
          <p style="font-size:15px; color:#166534; margin-bottom:14px;">Your Score: <strong>${scorePct}%</strong> (${correctCount} out of ${questions.length} correct)</p>
          <button class="btn-primary" onclick="AppRouter.renderQuiz(document.getElementById('page-container'))">Retake / New Test</button>
        </div>
      `;
      target.insertAdjacentHTML('afterbegin', reportHtml);
    }
  },

  // 8. BOOKMARKS VIEW
  renderBookmarks(container) {
    const bookmarkedIds = AppStore.getBookmarks();
    let cardsHtml = '';

    bookmarkedIds.forEach(id => {
      const info = this.findTopic(id);
      if (info) {
        cardsHtml += `
          <div class="subject-card" style="margin-bottom:14px;">
            <div class="subject-card-header">
              <span class="subject-code">${info.subject_code} • Mod ${info.module_no}</span>
              <button class="btn-secondary-sm" onclick="AppStore.toggleBookmark('${id}'); AppRouter.handleRoute();">Remove ★</button>
            </div>
            <h3 class="subject-name">${info.topic.title}</h3>
            <p class="subject-desc">${info.topic.intro.definition}</p>
            <div style="margin-top:auto;">
              <a href="#topic/${id}" class="btn-primary" style="font-size:12px; padding:6px 14px;">Study Lesson →</a>
            </div>
          </div>
        `;
      }
    });

    if (bookmarkedIds.length === 0) {
      cardsHtml = `<div class="hero-card"><p>No bookmarks saved yet. Click '☆ Bookmark Topic' on any lesson to save it here for fast revision.</p></div>`;
    }

    container.innerHTML = `
      <div style="margin-bottom:24px;">
        <h1 class="section-title">⭐ Bookmarked Lessons (${bookmarkedIds.length})</h1>
        <p style="font-size:14px; color:var(--text-secondary); margin-top:4px;">Quick access to lessons you have marked for examination revision.</p>
      </div>
      <div>${cardsHtml}</div>
    `;
  },

  // Helper to locate a topic across all subjects
  findTopic(topicId) {
    for (let sIdx = 0; sIdx < DATA.curriculum.subjects.length; sIdx++) {
      const s = DATA.curriculum.subjects[sIdx];
      for (let mIdx = 0; mIdx < s.modules.length; mIdx++) {
        const m = s.modules[mIdx];
        for (let tIdx = 0; tIdx < (m.topics || []).length; tIdx++) {
          if (m.topics[tIdx].id === topicId) {
            // Find prev & next
            let prev = null;
            let next = null;
            if (tIdx > 0) prev = m.topics[tIdx - 1];
            if (tIdx < m.topics.length - 1) next = m.topics[tIdx + 1];

            return {
              subject_id: s.id,
              subject_code: s.code,
              subject_name: s.name,
              module_no: m.module_no,
              topic: m.topics[tIdx],
              prev: prev,
              next: next
            };
          }
        }
      }
    }
    return null;
  },

  escapeHtml(str) {
    if (!str) return '';
    return str.replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  },

  // Global Search Modal Engine
  initSearch() {
    window.addEventListener('keydown', (e) => {
      if ((e.ctrlKey && e.key === 'k') || (e.key === '/' && document.activeElement.tagName !== 'INPUT')) {
        e.preventDefault();
        this.openSearch();
      }
      if (e.key === 'Escape') {
        this.closeSearch();
      }
    });

    const searchInput = document.getElementById('search-input-field');
    if (searchInput) {
      searchInput.addEventListener('input', (e) => this.performSearch(e.target.value));
    }
  },

  openSearch() {
    const modal = document.getElementById('search-modal-overlay');
    if (modal) {
      modal.classList.add('active');
      const input = document.getElementById('search-input-field');
      if (input) {
        input.value = '';
        input.focus();
        this.performSearch('');
      }
    }
  },

  closeSearch() {
    const modal = document.getElementById('search-modal-overlay');
    if (modal) modal.classList.remove('active');
  },

  performSearch(query) {
    const list = document.getElementById('search-results-list');
    if (!list) return;

    const q = query.trim().toLowerCase();
    if (!q) {
      list.innerHTML = `<li style="padding:20px; color:var(--text-secondary); text-align:center; font-size:13px;">Type keywords to search topics, model exams, and practical labs...</li>`;
      return;
    }

    let results = [];

    // Search Topics
    DATA.curriculum.subjects.forEach(s => {
      s.modules.forEach(m => {
        (m.topics || []).forEach(t => {
          if (t.title.toLowerCase().includes(q) || t.intro.definition.toLowerCase().includes(q)) {
            results.push({
              type: 'TOPIC',
              title: t.title,
              sub: `${s.code} • Module ${m.module_no}`,
              link: `#topic/${t.id}`
            });
          }
        });
      });
    });

    // Search Exams
    DATA.flat_exams.forEach(e => {
      if (e.title.toLowerCase().includes(q) || e.intro.definition.toLowerCase().includes(q)) {
        results.push({
          type: 'EXAM',
          title: `Q${e.question_no}: ${e.title}`,
          sub: `${e.subject_id.toUpperCase()} Model Answer`,
          link: `#exams/${e.subject_id}`
        });
      }
    });

    // Search Labs
    ['bcac591', 'bcac592'].forEach(labId => {
      (DATA.practicals[labId] || []).forEach(c => {
        if (c.title.toLowerCase().includes(q) || c.objective.toLowerCase().includes(q)) {
          results.push({
            type: 'LAB',
            title: c.title,
            sub: `${c.code} Lab Case Study`,
            link: `#practicals/${labId}`
          });
        }
      });
    });

    if (results.length === 0) {
      list.innerHTML = `<li style="padding:20px; color:var(--text-secondary); text-align:center; font-size:13px;">No results found for "${query}".</li>`;
      return;
    }

    list.innerHTML = results.slice(0, 15).map(r => `
      <li class="search-result-item" onclick="AppRouter.closeSearch(); window.location.hash='${r.link}'">
        <span class="search-res-type">${r.type}</span>
        <div class="search-res-title">${r.title}</div>
        <div class="search-res-sub">${r.sub}</div>
      </li>
    `).join('');
  }
};

// Initialize app when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  AppRouter.init();
});
"""
