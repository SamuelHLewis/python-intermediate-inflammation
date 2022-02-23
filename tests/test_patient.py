"""Tests for the Patient model."""


def test_create_patient():
    from inflammation.models import Patient

    name = 'Alice'
    p = Patient(name=name)

    assert p.name == name

def test_create_doctor():
    from inflammation.models import Doctor

    name = 'Dr Nick'
    d = Doctor(name=name)

    assert str(d) == name

def test_doctor_add_patient():
    from inflammation.models import Doctor, Patient

    d_name = 'Dr Nick'
    p_name = 'Angela'

    d = Doctor(d_name)
    p = Patient(p_name)

    d.add_patient(p)
    assert d.patients == [p]

def test_doctor_assign_to_trial():
    from inflammation.models import Doctor

    name = 'Dr Nick'
    trial = 'psoriasis101'

    d = Doctor(name)
    d.assign_to_trial(trial)

    assert d.trials == [trial]