const stripePublicKey = JSON.parse(
    document.getElementById('id_stripe_public_key').textContent
);
const clientSecret = JSON.parse(
    document.getElementById('id_client_secret').textContent
);

const stripe = Stripe(stripePublicKey);

const appearance = {
    theme: "night",
    variables: {
        colorPrimary: "#4da3ff",
        colorBackground: "#17181a",
        colorText: "#f5f5f5",
        colorDanger: "#ff9f9f",
        colorTextPlaceholder: "#8c9198",
        fontFamily: "Roboto, Arial, sans-serif",
        spacingUnit: "4px",
        borderRadius: "8px",
    },
    rules: {
        ".Input": {
            backgroundColor: "#17181a",
            border: "1ppx solid #525866",
            boxShadow: "none",
        },
        ".Input:focus": {
            border: "1px solid #4da3ff",
            boxShadow: "0 0 0 2pc rgba(77, 163, 255, 0.2)",
        },
        ".Label": {
            color: "#f5f5f5",
        },
        ".Error": {
            color: "#ff9f9f",
        },
    },
};

const elements = stripe.elements({
    clientSecret: clientSecret,
    appearance: appearance,
});

const paymentElement = elements.create("payment", {
    defaultValues: {
        billingDetails: {
            name: document.getElementById("id_full_name")?.value || "",
            email: document.getElementById("id_email")?.value || "",
            phone: document.getElementById("id_phone_number")?.value || "",
            address: {
                line1: document.getElementById("id_street_address1")?.value || "",
                line2: document.getElementById("id_street_address2")?.value || "",
                city: document.getElementById("id_town_or_city")?.value || "",
                state: document.getElementById("id_county")?.value || "",
                country: document.getElementById("id_country_code")?.value || "",
                postal_code: document.getElementById("id_postcode")?.value || "",
            },
        },
    },
    fields: {
        billingDetails: {
            name: "never",
            email: "never",
            phone: "never",
            address: "never",
        },
    },
});

paymentElement.mount("#payment-element");

paymentElement.on("change", function(event) {
    const errorDiv = document.getElementById("payment-errors");

    if (event.error) {
        errorDiv.textContent = event.error.message;
    } else {
        errorDiv.textContent = "";
    }
});

const form = document.getElementById("payment-form");
const submitButton = document.getElementById("submit-button");
const errorDiv = document.getElementById("payment-errors");

form.addEventListener("submit", async function(event) {
    event.preventDefault();

    submitButton.disabled = true;
    errorDiv.textContent = "";

    const { error, paymentIntent } = await stripe.confirmPayment({
        elements,
        confirmParams: {
            return_url: `${window.location.origin}/checkout/`,
            payment_method_data: {
                billing_details: {
                    name: document.getElementById("id_full_name")?.value || "",
                    email: document.getElementById("id_email")?.value || "",
                    phone: document.getElementById("id_phone_number")?.value || "",
                    address: {
                        line1: document.getElementById("id_street_address1")?.value || "",
                        line2: document.getElementById("id_street_address2")?.value || "",
                        city: document.getElementById("id_town_or_city")?.value || "",
                        state: document.getElementById("id_county")?.value || "",
                        country: document.getElementById("id_country_code")?.value || "",
                        postal_code: document.getElementById("id_postcode")?.value || "",
                    },
                },
            },
        },
        redirect: "if_required",
    });

    if (error) {
        errorDiv.textContent = error.message;
        submitButton.disabled = false;
        return;
    }

    if (paymentIntent && paymentIntent.status === "succeeded") {
        form.submit();
    }
});