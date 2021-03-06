import pytest
from moz_sample.sample.sub.module2 import Module2


class TestModule2:
    @pytest.fixture()
    def module2(request):
        return Module2()

    def test_method(self, module2: Module2, capfd):
        module2.method()
        out, err = capfd.readouterr()
        assert out == "module2's method called.\n"
        assert err == ""
