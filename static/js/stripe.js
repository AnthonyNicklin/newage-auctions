
const stripe = Stripe(pk);
    
// $('document').ready(function() {
//     stripe.redirectToCheckout({
//     // Make the id field from the Checkout Session creation API response
//     // available to this file, so you can provide it as parameter here
//     // instead of the {{CHECKOUT_SESSION_ID}} placeholder.
//     sessionId: sessionId
//     }).then(function (result) {
//     // If `redirectToCheckout` fails due to a browser or network
//     // error, display the localized error message to your customer
//     // using `result.error.message`.
//     });
// });

$(function(){
    $('#payment-form').submit(function(){
        var form = this ;
        console.log(form)
        var card = {
            number: $('#id_credit_card_number').val(),
            expMonth: $('#id_expiry_month').val(),
            expYear: $('#id_expiry_year').val(),
            cvc: $('#id_cvv').val()
        };
    Stripe.createToken(card, function(status, response){
        if (status === 200){
            $('#credit-card-errors').hide();
            $('#id_stripe_id').val(response.id);
            // Hide the details of the form from being submitted to our server
            $('#id_credit_card_number').removeAttr('name');
            $('#id_cvv').removeAttr('name');
            $('#id_expiry_month').removeAttr('name');
            $('#id_expiry_year').removeAttr('name');

            form.submit();
        }else {
            $('#stripe-error-message').text(response.error);
            $('#credit-card-errors').show();
            $('#validate_card_btn').attr('disabled', false);
        }
    });
    return false;
    });
});