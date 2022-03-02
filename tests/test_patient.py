"""Tests for the Patient model."""


def test_create_patient():
    """Test if Patient class creates Patient object correctly"""
    from inflammation.models import Patient

    name = 'Alice'
    p = Patient(name=name)

    assert p.name == name

def test_create_doctor():
    """Test if Doctor class creates Doctor object correctly"""
    from inflammation.models import Doctor

    name = 'Dr Nick'
    d = Doctor(name=name)

    assert str(d) == name

def test_doctor_add_patient():
    """Test if method add_patient() of Doctor class adds Patient object correctly"""
    from inflammation.models import Doctor, Patient

    d_name = 'Dr Nick'
    p_name = 'Angela'

    d = Doctor(d_name)
    p = Patient(p_name)

    d.add_patient(p)
    assert d.patients == [p]

def test_doctor_assign_to_trial():
    """Test if method assign_to_trial() of Doctor class assigns trial_name to trial list correctly"""
    from inflammation.models import Doctor

    name = 'Dr Nick'
    trial = 'psoriasis101'

    d = Doctor(name)
    d.assign_to_trial(trial)

    assert d.trials == [trial]