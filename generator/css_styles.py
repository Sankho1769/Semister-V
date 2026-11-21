# Complete Modern CSS Stylesheet for MAKAUT Academic Platform
def get_css():
    return """
:root {
  /* Brand Palette */
  --primary-blue: #8DB9F0;
  --vibrant-blue: #377FE6;
  --lavender: #E9E8F8;
  --violet: #786CE5;
  --peach: #F5B69E;
  --coral: #EF846B;
  --teal: #28A994;
  --yellow: #F2C75C;

  /* Supporting Surfaces & Neutrals */
  --bg-page: #F7F8FC;
  --bg-surface: #FFFFFF;
  --text-primary: #19283D;
  --text-secondary: #617087;
  --border-color: #E5E9F1;
  --success: #369B72;
  --error: #D65F64;

  /* Typography & Layout */
  --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  --font-mono: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  --sidebar-width: 270px;
  --header-height: 64px;
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --shadow-sm: 0 1px 3px rgba(25, 40, 61, 0.05);
  --shadow-md: 0 4px 12px rgba(25, 40, 61, 0.08);
  --shadow-lg: 0 10px 24px rgba(25, 40, 61, 0.12);
  --transition: all 0.2s ease-in-out;
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  font-size: 16px;
  scroll-behavior: smooth;
}

body {
  font-family: var(--font-sans);
  background-color: var(--bg-page);
  color: var(--text-primary);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* App Layout Grid */
.app-container {
  display: flex;
  min-height: 100vh;
}

/* Sidebar Navigation */
.sidebar {
  width: var(--sidebar-width);
  background: var(--bg-surface);
  border-right: 1px solid var(--border-color);
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  z-index: 100;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
}

.sidebar-header {
  padding: 20px;
  border-bottom: 1px solid var(--border-color);
  display: flex;
  align-items: center;
  gap: 12px;
}

.brand-badge {
  width: 38px;
  height: 38px;
  border-radius: var(--radius-sm);
  background: linear-gradient(135deg, var(--vibrant-blue), var(--violet));
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 18px;
  box-shadow: 0 2px 6px rgba(55, 127, 230, 0.3);
}

.brand-text h1 {
  font-size: 15px;
  font-weight: 700;
  color: var(--text-primary);
  line-height: 1.2;
}

.brand-text span {
  font-size: 11px;
  color: var(--text-secondary);
  font-weight: 500;
}

.nav-menu {
  list-style: none;
  padding: 16px 12px;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.nav-section-title {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  color: var(--text-secondary);
  padding: 12px 12px 6px;
}

.nav-item a {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 14px;
  border-radius: var(--radius-sm);
  color: var(--text-secondary);
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  transition: var(--transition);
}

.nav-item a:hover {
  background: var(--lavender);
  color: var(--vibrant-blue);
}

.nav-item.active a {
  background: var(--lavender);
  color: var(--vibrant-blue);
  font-weight: 700;
  border-left: 3px solid var(--vibrant-blue);
}

.nav-item .badge {
  margin-left: auto;
  font-size: 11px;
  padding: 2px 6px;
  border-radius: 10px;
  background: #E5E9F1;
  color: var(--text-secondary);
  font-weight: 600;
}

.nav-item.active .badge {
  background: var(--vibrant-blue);
  color: #fff;
}

.sidebar-footer {
  margin-top: auto;
  padding: 16px;
  border-top: 1px solid var(--border-color);
  font-size: 12px;
  color: var(--text-secondary);
}

/* Main Content Area */
.main-wrapper {
  margin-left: var(--sidebar-width);
  flex: 1;
  display: flex;
  flex-direction: column;
  min-width: 0;
}

/* Top App Header */
.top-header {
  height: var(--header-height);
  background: var(--bg-surface);
  border-bottom: 1px solid var(--border-color);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 28px;
  position: sticky;
  top: 0;
  z-index: 90;
}

.search-trigger {
  display: flex;
  align-items: center;
  gap: 10px;
  background: var(--bg-page);
  border: 1px solid var(--border-color);
  padding: 8px 16px;
  border-radius: 20px;
  color: var(--text-secondary);
  font-size: 13px;
  cursor: pointer;
  min-width: 280px;
  transition: var(--transition);
}

.search-trigger:hover {
  border-color: var(--primary-blue);
  background: #fff;
}

.search-shortcut {
  margin-left: auto;
  background: #E5E9F1;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 11px;
  font-family: var(--font-mono);
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 16px;
}

.progress-pill {
  display: flex;
  align-items: center;
  gap: 8px;
  background: var(--lavender);
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 700;
  color: var(--violet);
}

.btn-secondary-sm {
  background: #fff;
  border: 1px solid var(--border-color);
  color: var(--text-primary);
  padding: 6px 12px;
  border-radius: var(--radius-sm);
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition);
}

.btn-secondary-sm:hover {
  background: var(--bg-page);
  border-color: #cbd5e1;
}

/* Page Content Container */
.page-container {
  padding: 28px;
  max-width: 1240px;
  margin: 0 auto;
  width: 100%;
}

/* Hero Section */
.hero-card {
  background: linear-gradient(135deg, #FFFFFF 0%, var(--lavender) 100%);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  padding: 32px;
  margin-bottom: 28px;
  position: relative;
  overflow: hidden;
  box-shadow: var(--shadow-sm);
}

.hero-tag {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: var(--vibrant-blue);
  color: #fff;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  padding: 4px 10px;
  border-radius: 12px;
  margin-bottom: 14px;
}

.hero-title {
  font-size: 26px;
  font-weight: 800;
  color: var(--text-primary);
  margin-bottom: 8px;
}

.hero-subtitle {
  font-size: 14px;
  color: var(--text-secondary);
  max-width: 720px;
  margin-bottom: 20px;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 16px;
  margin-top: 20px;
}

.stat-box {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 16px;
  display: flex;
  flex-direction: column;
}

.stat-num {
  font-size: 26px;
  font-weight: 800;
  color: var(--vibrant-blue);
}

.stat-label {
  font-size: 12px;
  color: var(--text-secondary);
  font-weight: 600;
}

/* Section Header */
.section-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
}

.section-title {
  font-size: 18px;
  font-weight: 700;
  color: var(--text-primary);
  display: flex;
  align-items: center;
  gap: 8px;
}

/* Subject Grid */
.subject-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 20px;
  margin-bottom: 32px;
}

.subject-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 22px;
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
  transition: var(--transition);
  position: relative;
}

.subject-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
  border-color: var(--primary-blue);
}

.subject-card-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  margin-bottom: 12px;
}

.subject-code {
  font-family: var(--font-mono);
  font-size: 12px;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 4px;
  background: var(--lavender);
  color: var(--violet);
}

.subject-credits {
  font-size: 11px;
  font-weight: 600;
  color: var(--text-secondary);
}

.subject-name {
  font-size: 16px;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 8px;
  line-height: 1.3;
}

.subject-desc {
  font-size: 13px;
  color: var(--text-secondary);
  margin-bottom: 16px;
  flex: 1;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.subject-meta-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 16px;
}

.meta-chip {
  font-size: 11px;
  background: var(--bg-page);
  border: 1px solid var(--border-color);
  padding: 2px 8px;
  border-radius: 12px;
  color: var(--text-secondary);
}

.card-progress-bar {
  height: 6px;
  background: #E5E9F1;
  border-radius: 3px;
  overflow: hidden;
  margin-bottom: 14px;
}

.card-progress-fill {
  height: 100%;
  background: var(--vibrant-blue);
  border-radius: 3px;
  transition: width 0.3s ease;
}

.btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  background: var(--vibrant-blue);
  color: #fff;
  border: none;
  padding: 10px 18px;
  border-radius: var(--radius-sm);
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  text-decoration: none;
  transition: var(--transition);
}

.btn-primary:hover {
  background: #2563eb;
}

.btn-outline {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  background: transparent;
  color: var(--text-primary);
  border: 1px solid var(--border-color);
  padding: 9px 16px;
  border-radius: var(--radius-sm);
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  text-decoration: none;
  transition: var(--transition);
}

.btn-outline:hover {
  background: var(--bg-page);
  border-color: #cbd5e1;
}

/* Topic Learning Lesson Styling (Section A) */
.lesson-container {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  padding: 36px;
  box-shadow: var(--shadow-sm);
}

.lesson-header {
  border-bottom: 1px solid var(--border-color);
  padding-bottom: 24px;
  margin-bottom: 28px;
}

.lesson-breadcrumbs {
  font-size: 12px;
  color: var(--text-secondary);
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 12px;
}

.lesson-breadcrumbs a {
  color: var(--vibrant-blue);
  text-decoration: none;
}

.lesson-title {
  font-size: 24px;
  font-weight: 800;
  color: var(--text-primary);
  line-height: 1.3;
  margin-bottom: 14px;
}

.lesson-subtopics {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.subtopic-pill {
  font-size: 12px;
  background: var(--lavender);
  color: var(--violet);
  padding: 3px 10px;
  border-radius: 12px;
  font-weight: 600;
}

/* 8-Part Lesson Section Layout */
.lesson-section {
  margin-bottom: 36px;
}

.lesson-section-title {
  font-size: 17px;
  font-weight: 700;
  color: var(--text-primary);
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 16px;
  padding-bottom: 8px;
  border-bottom: 2px solid var(--lavender);
}

.lesson-section-title span.part-badge {
  background: var(--violet);
  color: #fff;
  font-size: 11px;
  font-weight: 800;
  padding: 2px 7px;
  border-radius: 4px;
}

.prose {
  font-size: 15px;
  color: var(--text-primary);
  line-height: 1.7;
}

.prose p {
  margin-bottom: 14px;
}

.prose ul, .prose ol {
  margin-left: 24px;
  margin-bottom: 16px;
}

.prose li {
  margin-bottom: 6px;
}

/* Terminology Cards */
.term-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 12px;
  margin-top: 14px;
}

.term-card {
  background: var(--bg-page);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-sm);
  padding: 12px 14px;
}

.term-name {
  font-size: 13px;
  font-weight: 700;
  color: var(--vibrant-blue);
  margin-bottom: 4px;
  font-family: var(--font-mono);
}

.term-def {
  font-size: 12px;
  color: var(--text-secondary);
  line-height: 1.4;
}

/* Comparison Tables */
.data-table-wrapper {
  overflow-x: auto;
  margin: 16px 0;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-sm);
}

.data-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
  text-align: left;
}

.data-table th {
  background: var(--bg-page);
  color: var(--text-primary);
  font-weight: 700;
  padding: 10px 14px;
  border-bottom: 1px solid var(--border-color);
}

.data-table td {
  padding: 10px 14px;
  border-bottom: 1px solid var(--border-color);
  color: var(--text-secondary);
}

.data-table tr:last-child td {
  border-bottom: none;
}

.data-table tr:hover {
  background: #fbfcfe;
}

/* Code Display Block */
.code-container {
  background: #19283D;
  border-radius: var(--radius-sm);
  margin: 16px 0;
  overflow: hidden;
  box-shadow: var(--shadow-sm);
}

.code-header {
  background: #131E2E;
  padding: 8px 14px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  color: #94a3b8;
  font-size: 12px;
  font-family: var(--font-mono);
}

.btn-copy {
  background: transparent;
  border: 1px solid #334155;
  color: #cbd5e1;
  padding: 3px 8px;
  border-radius: 4px;
  font-size: 11px;
  cursor: pointer;
  transition: var(--transition);
}

.btn-copy:hover {
  background: #334155;
  color: #fff;
}

.code-pre {
  padding: 16px;
  color: #E2E8F0;
  font-family: var(--font-mono);
  font-size: 13px;
  line-height: 1.5;
  overflow-x: auto;
}

/* Scientific Diagram Container */
.diagram-container {
  background: #fff;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 20px;
  margin: 20px 0;
  text-align: center;
}

.diagram-caption {
  margin-top: 12px;
  font-size: 12px;
  color: var(--text-secondary);
  font-weight: 600;
  font-style: italic;
}

/* Alerts / Callouts */
.alert-box {
  padding: 14px 16px;
  border-radius: var(--radius-sm);
  margin: 16px 0;
  display: flex;
  gap: 12px;
  font-size: 13px;
  line-height: 1.5;
}

.alert-tip {
  background: #F0FDF4;
  border: 1px solid #BBF7D0;
  color: #166534;
}

.alert-warning {
  background: #FFFBEB;
  border: 1px solid #FDE68A;
  color: #92400E;
}

.alert-danger {
  background: #FEF2F2;
  border: 1px solid #FECACA;
  color: #991B1B;
}

/* Learning Actions Bar */
.actions-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 24px;
  margin-top: 36px;
  border-top: 1px solid var(--border-color);
  flex-wrap: wrap;
  gap: 12px;
}

.action-buttons-group {
  display: flex;
  gap: 10px;
}

/* Section B: Model Examination Cards */
.exam-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 24px;
  margin-bottom: 24px;
  box-shadow: var(--shadow-sm);
}

.exam-card-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 18px;
  padding-bottom: 14px;
  border-bottom: 1px solid var(--border-color);
}

.exam-q-num {
  font-size: 12px;
  font-weight: 800;
  color: var(--vibrant-blue);
  background: var(--lavender);
  padding: 3px 8px;
  border-radius: 4px;
  white-space: nowrap;
}

.exam-q-title {
  font-size: 17px;
  font-weight: 700;
  color: var(--text-primary);
  flex: 1;
}

.exam-part-label {
  font-size: 11px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.6px;
  color: var(--violet);
  margin-bottom: 6px;
}

.exam-point-item {
  background: var(--bg-page);
  border-left: 3px solid var(--vibrant-blue);
  padding: 12px 16px;
  border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
  margin-bottom: 12px;
}

.exam-point-heading {
  font-size: 14px;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 4px;
}

.exam-point-desc {
  font-size: 13px;
  color: var(--text-secondary);
  line-height: 1.5;
  margin-bottom: 6px;
}

.exam-point-meta {
  font-size: 12px;
  color: var(--text-secondary);
}

.exam-point-meta strong {
  color: var(--vibrant-blue);
}

/* Section C: Interactive Quiz View */
.quiz-config-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  padding: 32px;
  margin-bottom: 28px;
  box-shadow: var(--shadow-sm);
}

.filter-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 16px;
  margin-top: 16px;
}

.form-group label {
  display: block;
  font-size: 12px;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 6px;
}

.form-select {
  width: 100%;
  padding: 10px 14px;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-sm);
  background: #fff;
  font-size: 14px;
  color: var(--text-primary);
  outline: none;
  transition: var(--transition);
}

.form-select:focus {
  border-color: var(--vibrant-blue);
  box-shadow: 0 0 0 3px rgba(55, 127, 230, 0.15);
}

.quiz-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 24px;
  margin-bottom: 20px;
  box-shadow: var(--shadow-sm);
}

.quiz-meta-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--text-secondary);
  margin-bottom: 12px;
}

.quiz-question-text {
  font-size: 16px;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 16px;
  line-height: 1.4;
}

.options-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.option-item {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 12px 16px;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: var(--transition);
  font-size: 14px;
  color: var(--text-primary);
}

.option-item:hover {
  background: var(--bg-page);
  border-color: #cbd5e1;
}

.option-item.selected {
  background: var(--lavender);
  border-color: var(--vibrant-blue);
  color: var(--vibrant-blue);
  font-weight: 600;
}

.option-item.correct {
  background: #F0FDF4;
  border-color: #369B72;
  color: #166534;
}

.option-item.incorrect {
  background: #FEF2F2;
  border-color: #D65F64;
  color: #991B1B;
}

.explanation-card {
  background: #F8FAFC;
  border: 1px solid #E2E8F0;
  border-radius: var(--radius-sm);
  padding: 14px 16px;
  margin-top: 14px;
  font-size: 13px;
  line-height: 1.5;
  color: var(--text-secondary);
}

/* Viva Questions Accordion */
.viva-box {
  background: var(--bg-page);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-sm);
  padding: 14px 16px;
  margin-bottom: 10px;
}

.viva-q {
  font-size: 13px;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 6px;
}

.viva-a {
  font-size: 13px;
  color: var(--text-secondary);
  line-height: 1.5;
}

/* Global Search Modal */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(25, 40, 61, 0.45);
  backdrop-filter: blur(4px);
  z-index: 1000;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding: 80px 20px;
  opacity: 0;
  visibility: hidden;
  transition: var(--transition);
}

.modal-overlay.active {
  opacity: 1;
  visibility: visible;
}

.search-modal {
  width: 100%;
  max-width: 640px;
  background: #fff;
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-lg);
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.search-input-wrapper {
  display: flex;
  align-items: center;
  padding: 16px 20px;
  border-bottom: 1px solid var(--border-color);
  gap: 12px;
}

.search-input-field {
  flex: 1;
  border: none;
  font-size: 16px;
  color: var(--text-primary);
  outline: none;
}

.search-results-list {
  max-height: 400px;
  overflow-y: auto;
  list-style: none;
}

.search-result-item {
  padding: 12px 20px;
  border-bottom: 1px solid var(--border-color);
  cursor: pointer;
  transition: var(--transition);
}

.search-result-item:hover {
  background: var(--bg-page);
}

.search-res-type {
  font-size: 10px;
  font-weight: 700;
  text-transform: uppercase;
  padding: 2px 6px;
  border-radius: 4px;
  background: var(--lavender);
  color: var(--violet);
}

.search-res-title {
  font-size: 14px;
  font-weight: 600;
  color: var(--text-primary);
  margin-top: 4px;
}

.search-res-sub {
  font-size: 12px;
  color: var(--text-secondary);
}

/* Mobile Bottom Navigation Bar */
.bottom-nav {
  display: none;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 60px;
  background: var(--bg-surface);
  border-top: 1px solid var(--border-color);
  z-index: 100;
  align-items: center;
  justify-content: space-around;
}

.bottom-nav-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 3px;
  color: var(--text-secondary);
  text-decoration: none;
  font-size: 10px;
  font-weight: 600;
}

.bottom-nav-item.active {
  color: var(--vibrant-blue);
}

/* Responsive Media Queries */
@media (max-width: 992px) {
  :root {
    --sidebar-width: 220px;
  }
  .page-container {
    padding: 20px;
  }
}

@media (max-width: 768px) {
  .sidebar {
    display: none;
  }
  .main-wrapper {
    margin-left: 0;
    margin-bottom: 60px;
  }
  .bottom-nav {
    display: flex;
  }
  .top-header {
    padding: 0 16px;
  }
  .search-trigger {
    min-width: 180px;
  }
  .page-container {
    padding: 16px;
  }
  .hero-card {
    padding: 20px;
  }
  .hero-title {
    font-size: 20px;
  }
  .lesson-container {
    padding: 20px;
  }
}

/* Print Styling */
@media print {
  .sidebar, .top-header, .bottom-nav, .actions-bar, .search-trigger {
    display: none !important;
  }
  .main-wrapper {
    margin: 0 !important;
  }
  body {
    background: #fff;
    color: #000;
  }
}
"""
