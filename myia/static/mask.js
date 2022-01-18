var SPMaskBehavior = function (val) {
    return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
},
spOptions = {
    onKeyPress: function(val, e, field, options) {
        field.mask(SPMaskBehavior.apply({}, arguments), options);
    }
};


$(function(){
    $('.mask-cpf').mask('000.000.000-00', {reverse: true});
    $('.mask-phone').mask(SPMaskBehavior, spOptions);
    
});

django.jQuery(function(){
    django.jQuery('.mask-cpf').mask('000.000.000-00', {reverse: true});
    django.jQuery('.mask-phone').mask(SPMaskBehavior, spOptions);
    
});