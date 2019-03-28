$(function(){
  // initialize the validation for Submit Your ideas
  // Submit Your ideas has name attribute "submitIdea"
  $("form['submitIdea']").validate({
    //Validation Rules
    rules: {
      title: "required",
      summary: "required",
      description: "required",
      features: "required",
      businessImpact: "required",
      tangibleBenefits: "required",
    },
    message: {
      title: "Please enter the title for your idea",
      summary: "Please add some summary to your idea",
      description: "Please provide description to your idea",
      businessImpact: "Please provide details of business impact",
      tangibleBenefits: "Please give some benefits"
    },
    submitHandler: function(form){
      form.submit();
    }
  });
// choose the right button
  $('#btnGetValue').click(function() {
      var selValue = $('input[name=submitIdea.regulator]:checked').attr('id');
      $('p').html('<br/>Selected Radio Button ID is : <b>' + selValue + '</b>');
  });

});
