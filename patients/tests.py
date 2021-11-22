from datetime import date
from django.contrib.auth import get_user_model
from django.test import TestCase

from patients.models import Patient, Doctor, Appointment

User = get_user_model()


class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             email="testuser@invalid.com",
                                             password='asdasd')
        self.user.save()

    def test_user_exists(self):
        self.assertEqual(User.objects.all().count(), 1)

    def test_user_authentication(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302)

    def test_user_password(self):
        self.assertEqual(self.user.check_password('asdasd'), True)

    def test_user_props(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@invalid.com')
        self.assertEqual(self.user.is_staff, False)
        self.assertEqual(self.user.is_superuser, False)


class PatientTestCase(TestCase):
    def setUp(self):
        self.patient = Patient.objects.create(first_name='test',
                                              last_name='user',
                                              phone_no='1234567890',
                                              age='37')
        self.patient.save()

    def test_patient_exists(self):
        self.assertEqual(Patient.objects.all().count(), 1)

    def test_patient_props(self):
        self.assertEqual(self.patient.first_name, 'test')
        self.assertEqual(self.patient.last_name, 'user')
        self.assertEqual(self.patient.phone_no, '1234567890')
        self.assertEqual(self.patient.age, '37')
        self.assertEqual(self.patient.admitted_at, date.today())


class DoctorTestCase(TestCase):
    def setUp(self):
        self.doctor = Doctor.objects.create(first_name='test',
                                            last_name='user',
                                            phone_no='1234567890',
                                            age='37',
                                            email='testuser@invalid.com')
        self.doctor.save()

    def test_doctor_exists(self):
        self.assertEqual(Doctor.objects.all().count(), 1)

    def test_doctor_props(self):
        self.assertEqual(self.doctor.first_name, 'test')
        self.assertEqual(self.doctor.last_name, 'user')
        self.assertEqual(self.doctor.phone_no, '1234567890')
        self.assertEqual(self.doctor.age, '37')
        self.assertEqual(self.doctor.email, 'testuser@invalid.com')


class AppointmentTestCase(TestCase):
    def setUp(self):
        self.patient = Patient.objects.create(first_name='test',
                                              last_name='user',
                                              phone_no='1234567890',
                                              age='37')

        self.doctor = Doctor.objects.create(first_name='test',
                                            last_name='user',
                                            phone_no='1234567890',
                                            age='37',
                                            email='testuser@invalid.com')

        self.appointment = Appointment.objects.create(patient=self.patient,
                                                      doctor=self.doctor,
                                                      date='2017-01-01',
                                                      time='10:00')

        self.patient.save()
        self.doctor.save()
        self.appointment.save()

    def test_appointment_exists(self):
        self.assertEqual(Patient.objects.all().count(), 1)
        self.assertEqual(Doctor.objects.all().count(), 1)
        self.assertEqual(Appointment.objects.all().count(), 1)

    def test_appointment_props(self):
        self.assertEqual(self.appointment.patient, self.patient)
        self.assertEqual(self.appointment.doctor, self.doctor)
        self.assertEqual(self.appointment.date, '2017-01-01')
        self.assertEqual(self.appointment.time, '10:00')
