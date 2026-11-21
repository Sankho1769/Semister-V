# Helper for generating topic lessons
def create_topic(
    topic_id,
    title,
    subtopics,
    definition,
    background,
    importance,
    objectives,
    concepts,
    terminology,
    principles,
    structures,
    sequence,
    comp_headers,
    comp_rows,
    code_arch,
    svg_str,
    caption,
    scenario,
    sample_code,
    important_points,
    summary,
    key_terms,
    mechanisms,
    common_mistakes
):
    return {
        "id": topic_id,
        "title": title,
        "subtopics": subtopics,
        "intro": {
            "definition": definition,
            "background": background,
            "importance": importance,
            "objectives": objectives
        },
        "fundamentals": {
            "concepts": concepts,
            "terminology": [{"term": t[0], "definition": t[1]} for t in terminology],
            "principles": principles,
            "structures": structures
        },
        "detailed_explanation": {
            "sequence": sequence,
            "comparison_table": {
                "headers": comp_headers,
                "rows": comp_rows
            },
            "code_architecture": code_arch
        },
        "diagram": {
            "caption": caption,
            "svg": svg_str
        },
        "examples": {
            "scenario": scenario,
            "code": sample_code
        },
        "important_points": important_points,
        "revision": {
            "summary": summary,
            "terminology": key_terms,
            "mechanisms": mechanisms,
            "common_mistakes": common_mistakes
        }
    }
