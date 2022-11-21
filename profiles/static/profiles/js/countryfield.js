let countrySelected = $('#id_default_country').val();
if (!countrySelected) {
    $('#id_default_country').css('color', '#93979a');
}
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if (!countrySelected) {
        $(this).css('color', '#93979a');
    } else {
        $(this).css('color', '#000000');
    }
});