# Main Model Examination Questions Aggregator
from generator.exams_php import get_php_exams
from generator.exams_java import get_java_exams
from generator.exams_ent import get_ent_exams
from generator.exams_fm import get_fm_exams

def get_all_exams():
    return {
        "bcac501": get_php_exams(),
        "bcac502": get_java_exams(),
        "mim502": get_ent_exams(),
        "mim501": get_fm_exams()
    }

def get_flat_exams():
    res = []
    res.extend(get_php_exams())
    res.extend(get_java_exams())
    res.extend(get_ent_exams())
    res.extend(get_fm_exams())
    return res
