from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from golfproject import views as project_views
from employee import views as employee_views
from golfproject.views import (TournamentListView)
from django.contrib.auth.views import( LoginView,
                                       LogoutView,
                                       PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetConfirmView,
                                       PasswordResetCompleteView)
from employee.views import (EditPersonalDetailView,
                            EmployeeInfoCreateView,
                            NextOfKindCreateView,
                            NextOfKindEditView,
                            EmploymentInfoCreateView,
                            EmploymentInfoEditView,
                            EmploymentInfoDeleteView,
                            BankInfoCreateView,
                            BankInfoEditView,
                            CitizenshipCreateView,
                            CitizenshipEditView,
                            ResidentialInfoCreateView,
                            ResidentialInfoEditView
                            )

urlpatterns = [
    path('admin/dashboard/', project_views.admin_index_page, name='admin-index'),
    path('login/', LoginView.as_view(template_name='golfproject/pages/samples/login.html'), name='admin-login'),
    path('member/', project_views.members_page, name='admin-members'),
    path('member/edit/<int:id>/',project_views.edit_members_view, name='admin-member-edit'),
    path('members/create', project_views.create_member_view, name='create-member'),
    path('logout/', LogoutView.as_view(), name='admin-logout'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done /', PasswordResetCompleteView.as_view(), name='password-reset-complete-view'),
    path('user/profile/', project_views.user_profile_page, name='admin-profile'),
    path('add/tournaments/', project_views.add_tournament, name='admin-tournament'),
    path('all/tournaments/', TournamentListView.as_view(), name='user-tournaments'),
    path('tournaments/<int:tournament_id>/', project_views.tournament_detail, name='tournament-detail'),
    path('all/employees/', employee_views.view_employee_personal_info, name='employee-personal-info'),
    path('add/employee/', EmployeeInfoCreateView.as_view(), name='add-employee-info'),
    path('employee/<int:pk>/', EditPersonalDetailView.as_view(), name='edit-employee-info'),
    path('nextofkind/', employee_views.view_employee_nextOfKindInfo, name='next-of-kind-info'),
    path('add/nextofkind/', NextOfKindCreateView.as_view(), name='add-next-of-kind'),
    path('nextoofkind/<int:pk>/', NextOfKindEditView.as_view(), name='edit-next-of-kind'),
    path('employment/info/', employee_views.view_employee_employment_info, name='employment-info'),
    path('add/employment/', EmploymentInfoCreateView.as_view(), name='employment-info-add'),
    path('employment/edit/<int:pk>/', EmploymentInfoEditView.as_view(), name='employment-info-edit'),
    path('employment/<int:pk>/delete/', EmploymentInfoDeleteView.as_view(), name='employment-info-delete'),
    path('bankinfo/', employee_views.view_bank_info, name='employee-bank-info'),
    path('add/bankinfo/', BankInfoCreateView.as_view(), name='employee-bank-info-add'),
    path('bank/edit/<int:pk>/', BankInfoEditView.as_view(), name='employee-bank-info-edit'),
    path('citizenship/info/', employee_views.view_employee_citizenshipInfo, name='citizenship-info'),
    path('add/citizenship/', CitizenshipCreateView.as_view(), name='citizenship-add'),
    path('citizenship/<int:pk>/', CitizenshipEditView.as_view(), name='citizenship-edit'),
    path('residential/info/', employee_views.view_employee_residentialInfo, name='residential-info'),
    path('add/residential/', ResidentialInfoCreateView.as_view(), name='residential-info-create'),
    path('residential/<int:pk>/', ResidentialInfoEditView.as_view(), name='residential-edit'),
    path('admin/bookings/', project_views.admin_booking_view, name='admin-books-info'),
    path('user/tournaments/booking', project_views.tournament_detail_view, name='user-booking-details'),
    path('employee/profile/<int:pk>/', employee_views.employee_profile_view, name='employee-profile'),
    path('employee/info/export/',employee_views.export_employee_info, name='employee_info_export'),
    path('employment/info/export/', employee_views.export_employeement_info, name='employement_info_export'),
    path('nextofkind/info/export/', employee_views.export_next_of_kind_info, name='employement_nextofkind_export'),
    path('bank/info/export/', employee_views.export_bank_info, name='bank_info_export'),
    path('citizenship/info/export/', employee_views.export_citienship_info, name='citizenship_info_export'),
    path('areaofresident/info/export/', employee_views.export_areof_residence_info,
         name='areaof_residence_info_export'),
    # path('employees/upload/', ),
    path('employees/upload-file/', employee_views.upload_new_employees, name="upload-employees-file"),
    path('member/edit/<slug:pk>/', project_views.UpdateMember.as_view(), name="member-edit")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
