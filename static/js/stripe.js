$(function() {
  $("#payment-form").submit(function() {
      let form = this;
      let card = {
          number: $("#id_credit_card_number").val(),
          expMonth: $("#id_expiry_month").val(),
          expYear: $("#id_expiry_year").val(),
          cvc: $("#id_cvv").val()
      };

    if (card.number === "") {
        alert("The Card Number field cannot be empty.");
        return false;
    }
    if (card.number !== "") {
        if (!(/^[0-9]*$/.test(card.number))) {
            alert("Card Number field can only contain numbers.");
            return false;
        }
    }
    if (card.cvc === "") {
        alert("The CVC field cannot be empty.");
        return false;
    }
    if (card.cvc !== "") {
        if (!(/^[0-9]*$/.test(card.cvc))) {
            alert("CVC field can only contain numbers.");
            return false;
        }
    }
    let month = new Date();
    let thisMonth = month.getMonth() + 1;
    if (card.expMonth < thisMonth) {
        alert("Expiration date must be greater than today's date.");
        return false;
    }

    //Once validation is complete generate a stripe token 
    Stripe.createToken(card, function(status, response) {
        if (status === 200) {
            $("#credit-card-errors").hide();
            $("#id_stripe_id").val(response.id);

            // Prevent the credit card details from being submitted
            // to our server
            $("#id_credit_card_number").removeAttr('name');
            $("#id_cvv").removeAttr('name');
            $("#id_expiry_month").removeAttr('name');
            $("#id_expiry_year").removeAttr('name');

            form.submit();
        } else {
            $("#stripe-error-message").text(response.error.message);
            $("#credit-card-errors").show();
            $("#validate_card_btn").attr("disabled", false);
        }
    });
    return false;
    });
});