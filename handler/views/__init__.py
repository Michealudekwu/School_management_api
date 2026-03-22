from .users import get_user_details,create_student, create_teacher, update_student, update_teahcer, delete_student, delete_teacher
from .school_details import get_course,get_courses,delete_course,update_course,create_course
from .school_details import get_departments,delete_department,create_department,update_department,department_detail
from .school_details import create_level,level_detail,delete_level,update_level,get_levels
from .school_details import create_materials,update_material,get_material,all_materials,delete_material
from .school_details import create_topic,all_topics,get_topic,delete_topic,update_topic
from .assesments import exam_list_create, exam_detail, exam_questions_list_create, exam_question_detail
from .assesments import start_exam_view, submit_attempt, view_results
from .assesments import performance_view, progress_view
from .assesments import option_list_create, option_detail
from .forum import create_question, create_answer, answer_manager, question_manager,get_questions, get_answers