var SPMaskBehavior = function (val) {
    return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
},
spOptions = {
    onKeyPress: function(val, e, field, options) {
        field.mask(SPMaskBehavior.apply({}, arguments), options);
    }
};


$(function(){
    $('#id_cpf').mask('000.000.000-00', {reverse: true});
    $('#id_phone').mask(SPMaskBehavior, spOptions);

    $('.mask-cpf').mask('000.000.000-00', {reverse: true});
    $('person.phone').mask(SPMaskBehavior, spOptions);
    
    $('id_cpf').mask('000.000.000-00', {reverse: true});
    
    $('#object.cpf').mask('000.000.000-00', {reverse: true});
    $('object.cpf').mask('000.000.000-00', {reverse: true});
    $('.object.cpf').mask('000.000.000-00', {reverse: true});
    
    $('#mask-cpf').mask('000.000.000-00', {reverse: true});
    $('mask-cpf').mask('000.000.000-00', {reverse: true});
    $('.mask-cpf').mask('000.000.000-00', {reverse: true});
    
    $('#person.cpf').mask('000.000.000-00', {reverse: true});
    $('person.cpf').mask('000.000.000-00', {reverse: true});
    $('.person.cpf').mask('000.000.000-00', {reverse: true});
    
});



/*
django.jQuery(function(){
    django.jQuery('.mask-cpf').mask('000.000.000-00', {reverse: true});
    django.jQuery('.mask-phone').mask(SPMaskBehavior, spOptions);
    
});
*/