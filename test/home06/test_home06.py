from classes.home06 import home06 as h6


class Test:

    def test_should_calculate_distance(self):
        assert h6.points_distance([0, 1], [-3, 4]) == 4.24

    def test_should_calculate_bmi(self):
        assert h6.calculate_bmi(68, 1.65) == 24.98

    def test_should_return_bmi_status_niedowaga(self):
        assert h6.status_bmi(17) == 'niedowaga'

    def test_should_return_bmi_status_optimum(self):
        assert h6.status_bmi(19) == 'optimum'

    def test_should_return_bmi_status_nadwaga(self):
        assert h6.status_bmi(26) == 'nadwaga'

    def test_should_return_bmi_status_otylosc(self):
        assert h6.status_bmi(32) == 'otyłość'
