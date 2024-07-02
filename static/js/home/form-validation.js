document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("registrationForm");
  const password = document.getElementById("new-password");
  const passwordError = document.getElementById("password-error");
  const passwordValidMessage = document.getElementById(
    "password-valid-message"
  );

  const passwordPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,}$/;

  password.addEventListener("input", function () {
    if (!passwordPattern.test(password.value)) {
      passwordError.textContent =
        "La contraseña debe tener al menos 6 caracteres, incluyendo una letra mayúscula, una letra minúscula y un número.";
      passwordError.style.display = "block";
      passwordValidMessage.style.display = "none";
    } else {
      passwordError.style.display = "none";
      passwordValidMessage.textContent = "La contraseña es válida.";
      passwordValidMessage.style.display = "block";
    }
  });

  form.addEventListener("submit", function (event) {
    event.preventDefault(); // Evitar el envío del formulario

    let isValid = true;

    // Validar nombre
    const firstName = document.getElementById("first-name");
    if (firstName.value.trim() === "") {
      showError("first-name-error", "El nombre es obligatorio.");
      isValid = false;
    } else {
      hideError("first-name-error");
    }

    // Validar apellido
    const lastName = document.getElementById("last-name");
    if (lastName.value.trim() === "") {
      showError("last-name-error", "El apellido es obligatorio.");
      isValid = false;
    } else {
      hideError("last-name-error");
    }

    // Validar email
    const email = document.getElementById("email");
    if (!validateEmail(email.value)) {
      showError(
        "email-error",
        "Por favor, introduce un correo electrónico válido."
      );
      isValid = false;
    } else {
      hideError("email-error");
    }

    // Validar contraseña
    if (!passwordPattern.test(password.value)) {
      showError(
        "password-error",
        "La contraseña debe tener al menos 6 caracteres, incluyendo una letra mayúscula, una letra minúscula y un número."
      );
      isValid = false;
    } else {
      hideError("password-error");
    }

    // Validar edad
    const age = document.getElementById("age");
    if (age.value === "" || age.value < 13 || age.value > 120) {
      showError("age-error", "La edad debe estar entre 13 y 120 años.");
      isValid = false;
    } else {
      hideError("age-error");
    }

    // Validar referrer
    const referrer = document.getElementById("referrer");
    if (referrer.value === "") {
      showError("referrer-error", "Por favor, selecciona una opción.");
      isValid = false;
    } else {
      hideError("referrer-error");
    }

    // Validar términos y condiciones
    const terms = document.getElementById("terms-and-conditions");
    if (!terms.checked) {
      showError("terms-error", "Debes aceptar los términos y condiciones.");
      isValid = false;
    } else {
      hideError("terms-error");
    }

    if (isValid) {
      form.reset(); // Reiniciar el formulario si es válido
      alert(
        "Formulario completado correctamente. Por favor, vuelve a llenar el formulario."
      );
    }
  });

  function showError(elementId, message) {
    const element = document.getElementById(elementId);
    if (!element) {
      const errorElement = document.createElement("span");
      errorElement.id = elementId;
      errorElement.className = "error-message";
      errorElement.textContent = message;
      document
        .getElementById(elementId.replace("-error", ""))
        .parentElement.appendChild(errorElement);
    } else {
      element.textContent = message;
      element.style.display = "block";
    }
  }

  function hideError(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
      element.textContent = "";
      element.style.display = "none";
    }
  }

  function validateEmail(email) {
    const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return re.test(email);
  }
});
