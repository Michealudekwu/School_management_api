from handler.urls.user_urls import urlpatterns as users_patterns
from handler.urls.level_urls import urlpatterns as level_patterns
from handler.urls.department_urls import urlpatterns as department_patterns
from handler.urls.course_urls import urlpatterns as course_patterns
from handler.urls.exam_urls import urlpatterns as exam_patterns
from handler.urls.options_urls import urlpatterns as options_patterns
from handler.urls.submit_urls import urlpatterns as submit_patterns
from handler.urls.topic_urls import urlpatterns as topic_patterns
from handler.urls.material_urls import urlpatterns as materials_patterns
from handler.urls.analytics_urls import urlpatterns as analytics_patterns
from handler.urls.enroll_urls import urlpatterns as enroll_patterns
from handler.urls.q_and_a_urls import urlpatterns as forum_patterns

urlpatterns = (
    users_patterns +
    level_patterns +
    department_patterns +
    course_patterns +
    exam_patterns +
    options_patterns +
    submit_patterns +
    topic_patterns +
    materials_patterns +
    analytics_patterns +
    enroll_patterns +
    forum_patterns
)