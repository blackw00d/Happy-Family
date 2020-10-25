let SnippetLogin = function () {

    let login = $('#m_login');
    let displaySignUpForm = function () {
        login.removeClass('m-login--forget-password');
        login.removeClass('m-login--signin');
        login.addClass('m-login--signup');
        login.find('.m-login__signup').addClass('flipInX animated');
    }
    let displaySignInForm = function () {
        login.removeClass('m-login--forget-password');
        login.removeClass('m-login--signup');
        login.addClass('m-login--signin');
        login.find('.m-login__signin').addClass('flipInX animated');
    }
    let displayForgetPasswordForm = function () {
        login.removeClass('m-login--signin');
        login.removeClass('m-login--signup');
        login.addClass('m-login--forget-password');
        login.find('.m-login__forget-password').addClass('flipInX animated');
    }

    let handleFormSwitch = function () {
        $('#m_login_forget_password').click(function (e) {
            e.preventDefault();
            displayForgetPasswordForm();
        });
        $('#m_login_forget_password_cancel').click(function (e) {
            e.preventDefault();
            displaySignInForm();
        });
        $('#m_login_signup').click(function (e) {
            e.preventDefault();
            displaySignUpForm();
        });
        $('#m_login_signup_cancel').click(function (e) {
            e.preventDefault();
            displaySignInForm();
        });
    }
    let handleSignInFormSubmit = function () {
        $(".m-register-form input").on('keyup', function ()
        {
            let validator=$('.m-register-form').validate();
            validator.form();
        });
        $('#m_login_signin_submit').click(function (e) {
            e.preventDefault();
            let btn = $(this);
            let form = $(this).closest('form');
            form.validate();
            if (!form.valid()) {
                return;
            }
            btn.addClass('m-loader m-loader--right m-loader--light').attr('disabled', true);
            setTimeout(function () {
                form.submit();
                return;
            }, 500);
        });
    }
    let handleSignUpFormSubmit = function () {
        $('#m_login_signup_submit').click(function (e) {
            e.preventDefault();
            let btn = $(this);
            let form = $(this).closest('form');
            form.validate();
            if (!form.valid()) {
                return;
            }
            btn.addClass('m-loader m-loader--right m-loader--light').attr('disabled', true);
            setTimeout(function () {
                form.submit();
                return;
            }, 500);
        });
    }
    let handleForgetPasswordFormSubmit = function () {
        $('#m_login_forget_password_submit').click(function (e) {
            e.preventDefault();
            let btn = $(this);
            let form = $(this).closest('form');
            form.validate();
            if (!form.valid()) {
                return;
            }
            btn.addClass('m-loader m-loader--right m-loader--light').attr('disabled', true);
            setTimeout(function () {
                form.submit();
                return;
            }, 500);
        });
    }
    let handleForgetPasswordUpdateFormSubmit = function () {
        $('#m_login_forget_password_submit2').click(function (e) {
            e.preventDefault();
            let btn = $(this);
            let form = $(this).closest('form');
            form.validate();
            if (!form.valid()) {
                return;
            }
            btn.addClass('m-loader m-loader--right m-loader--light').attr('disabled', true);
            setTimeout(function () {
                form.submit();
                return;
            }, 500);
        });
    }

    $('.close').click(function () {
        $(this).parent().remove();
    });

    return {
        init: function () {
            handleFormSwitch();
            handleSignInFormSubmit();
            handleSignUpFormSubmit();
            handleForgetPasswordFormSubmit();
            handleForgetPasswordUpdateFormSubmit();
        }
    };
}();

jQuery(document).ready(function () {
    SnippetLogin.init();
});