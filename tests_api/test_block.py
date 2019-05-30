import pytest
from tests_api.utils.api import Api


class TestBlockMoney:
    @pytest.mark.Critical
    def test_01(self):
        """Sending request with all mandatory fields with valid values """
        assert 'True' == Api.requestBlock('test-01')

    @pytest.mark.Medium
    def test_02(self):
        """Send null value in Key field """
        assert 'ACCESS_DENIED' == Api.requestBlock('test-02')

    @pytest.mark.Medium
    def test_03(self):
        """Send special characters in Key field """
        assert 'ACCESS_DENIED' == Api.requestBlock('test-03')

    @pytest.mark.Critical
    def test_04(self):
        """Send null value  in OrderId  field """
        assert 'WRONG_PARAMS' == Api.requestBlock('test-04', charOrder='')

    @pytest.mark.Critical
    def test_05(self):
        """Check length of OrderId fields (len = 50)"""
        assert 'True' == Api.requestBlock('test-05', charOrder=50)

    @pytest.mark.Critical
    def test_06(self):
        """Check length of OrderId fields (len = 51)"""
        assert 'INTERNAL_ERROR' == Api.requestBlock('test-06', charOrder=51)

    @pytest.mark.Critical
    def test_07(self):
        """Send special characters in OrderId field """
        assert 'True' == Api.requestBlock('test-07', charOrder='~!@#$%%^&*()_+<>?/') or \
               'DUPLICATE_ORDER_ID' == Api.requestBlock('test-07', charOrder='~!@#$%%^&*()_+<>?/')

    @pytest.mark.Critical
    def test_08(self):
        """Send different values in OrderId fields """
        assert 'True' == Api.requestBlock('test-08', differentOrderId=True)

    @pytest.mark.Critical
    def test_09(self):
        """Send null value in Amount fields """
        assert 'AMOUNT_ERROR' == Api.requestBlock('test-09')

    @pytest.mark.Critical
    def test_10(self):
        """Send value with dot  in Amount fields """
        assert 'AMOUNT_ERROR' == Api.requestBlock('test-10')

    @pytest.mark.Critical
    def test_11(self):
        """Send different values in Amount fields """
        assert 'True' == Api.requestBlock('test-11')

    @pytest.mark.Critical
    def test_12(self):
        """Send null value  in PAN fields """
        assert 'WRONG_PAY_INFO' == Api.requestBlock('test-12')

    @pytest.mark.Critical
    def test_13(self):
        """Send special characters  in PAN fields """
        assert 'WRONG_PAN' == Api.requestBlock('test-13')

    @pytest.mark.Critical
    def test_14(self):
        """Send valid value with dot  in PAN fields """
        assert 'PAYMENT_ENGINE_ERROR' == Api.requestBlock('test-14')

    @pytest.mark.Critical
    def test_15(self):
        """Send null value in EMonth fields """
        assert 'WRONG_EXPIRE_DATE' == Api.requestBlock('test-15')

    @pytest.mark.Critical
    def test_16(self):
        """Send special characters in EMonth fields """
        assert 'WRONG_PAY_INFO' == Api.requestBlock('test-16')

    @pytest.mark.Critical
    def test_17(self):
        """Check EMonth field’s length (len = 1)"""
        assert 'True' == Api.requestBlock('test-17')

    @pytest.mark.Critical
    def test_18(self):
        """Check EMonth field’s length (len = 3)"""
        assert 'WRONG_EXPIRE_DATE' == Api.requestBlock('test-18')

    @pytest.mark.Critical
    def test_19(self):
        """Send boundary values EMonth field (EMonth= 12)"""
        assert 'True' == Api.requestBlock('test-19')

    @pytest.mark.Critical
    def test_20(self):
        """Send boundary values EMonth field (EMonth= 13)"""
        assert 'WRONG_EXPIRE_DATE' == Api.requestBlock('test-20')

    @pytest.mark.Critical
    def test_21(self):
        """Send boundary values EMonth field (EMonth= 00)"""
        assert 'WRONG_EXPIRE_DATE' == Api.requestBlock('test-21')

    @pytest.mark.Critical
    def test_22(self):
        """Send boundary values EMonth field (EMonth= 01)"""
        assert 'True' == Api.requestBlock('test-22')

    @pytest.mark.Critical
    def test_23(self):
        """Send null value in EYear field """
        assert 'CARD_EXPIRED' == Api.requestBlock('test-23')

    @pytest.mark.Critical
    def test_24(self):
        """Send special characters in EYear field """
        assert 'WRONG_PAY_INFO' == Api.requestBlock('test-24')

    @pytest.mark.Critical
    def test_25(self):
        """Check expired and current years (EYear = 18)"""
        assert 'CARD_EXPIRED' == Api.requestBlock('test-25')

    @pytest.mark.Critical
    def test_26(self):
        """Check expired and current years (EYear = 19)"""
        assert 'CARD_EXPIRED' == Api.requestBlock('test-26')

    @pytest.mark.Medium
    def test_27(self):
        """Send null value in CardHolder field """
        assert 'True' == Api.requestBlock('test-27')

    @pytest.mark.Medium
    def test_28(self):
        """Send numerical value in CardHolder field """
        assert 'True' == Api.requestBlock('test-28')

    @pytest.mark.Medium
    def test_29(self):
        """Check length of  CardHolder  field (len = 30)"""
        assert 'True' == Api.requestBlock('test-29')

    @pytest.mark.Medium
    def test_30(self):
        """"Check length of  CardHolder  field (len = 31)"""
        assert 'True' == Api.requestBlock('test-30')

    @pytest.mark.Medium
    def test_31(self):
        """Check length of  CardHolder  field (len = 29)"""
        assert 'True' == Api.requestBlock('test-31')

    @pytest.mark.Medium
    def test_32(self):
        """Send only spaces in CardHolder """
        assert 'True' == Api.requestBlock('test-32')

    @pytest.mark.Medium
    def test_33(self):
        """Send special characters in CardHolder """
        assert 'True' == Api.requestBlock('test-33')

    @pytest.mark.Critical
    def test_34(self):
        """Send null value  in SecureCode """
        assert 'True' == Api.requestBlock('test-34')

    @pytest.mark.Critical
    def test_35(self):
        """Send special characters  in SecureCode """
        assert 'True' == Api.requestBlock('test-35')

    @pytest.mark.Critical
    def test_36(self):
        """Check length of SecureCode (SecureCode= 1 )"""
        assert 'True' == Api.requestBlock('test-36')

    @pytest.mark.Critical
    def test_37(self):
        """Check length of SecureCode (SecureCode= 12 )"""
        assert 'True' == Api.requestBlock('test-37')

    @pytest.mark.Critical
    def test_38(self):
        """Check length of SecureCode (SecureCode= 123 )"""
        assert 'True' == Api.requestBlock('test-38')

    @pytest.mark.Critical
    def test_39(self):
        """Check length of SecureCode (SecureCode= 1234 )"""
        assert 'True' == Api.requestBlock('test-39')

    @pytest.mark.Critical
    def test_40(self):
        """Check length of SecureCode (SecureCode= 12345 )"""
        assert 'True' == Api.requestBlock('test-40')

    @pytest.mark.Minor
    def test_41(self):
        """Send null value  in PaytureId """
        assert 'True' == Api.requestBlock('test-41')

    @pytest.mark.Minor
    def test_42(self):
        """Check length of  PaytureId (len= 50)"""
        assert 'True' == Api.requestBlock('test-42')

    @pytest.mark.Minor
    def test_43(self):
        """Check length of  PaytureId (len= 51)"""
        assert 'True' == Api.requestBlock('test-43')

    @pytest.mark.Minor
    def test_44(self):
        """Send null value  in CustomerKey """
        assert 'True' == Api.requestBlock('test-44')

    @pytest.mark.Minor
    def test_45(self):
        """Check length of  CustomerKey (len= 50)"""
        assert 'True' == Api.requestBlock('test-45')

    @pytest.mark.Minor
    def test_46(self):
        """Check length of  CustomerKey (len= 51)"""
        assert 'True' == Api.requestBlock('test-46')

    @pytest.mark.Minor
    def test_47(self):
        """Send null value  in IP """
        assert 'ACCESS_DENIED' == Api.requestBlock('test-47', CustomFields=True)

    @pytest.mark.Minor
    def test_48(self):
        """Send some letters value  in IP"""
        assert 'True' == Api.requestBlock('test-48', CustomFields=True)

    @pytest.mark.Minor
    def test_49(self):
        """Send value without dots  in IP"""
        assert 'True' == Api.requestBlock('test-49', CustomFields=True)

    @pytest.mark.Minor
    def test_50(self):
        """Send dots in wrong places e  in IP"""
        assert 'True' == Api.requestBlock('test-50', CustomFields=True)

    @pytest.mark.Minor
    def test_51(self):
        """Send null value  in Description"""
        assert 'True' == Api.requestBlock('test-51', CustomFields=True)

    @pytest.mark.Minor
    def test_52(self):
        """Send null value  in Cheque  field"""
        assert 'True' == Api.requestBlock('test-52')


