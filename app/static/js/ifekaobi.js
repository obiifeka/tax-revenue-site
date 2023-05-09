  var dropdownElementList = [].slice.call(document.querySelectorAll('.dropdown-toggle'))
  var dropdownList = dropdownElementList.map(function (dropdownToggleEl) {
    return new bootstrap.Dropdown(dropdownToggleEl)
  })

  const leadForm = document.getElementById('lead-form');
  const submitButton = leadForm.querySelector('button[type="submit"]');
  
  submitButton.addEventListener('click', function(event) {
    if (!leadForm.checkValidity()) {
      event.preventDefault();
      submitButton.classList.add('btn-slide');
      setTimeout(function() {
        submitButton.classList.remove('btn-slide');
      }, 1000);
    }
  });

  
  