console.log("datepicker ok") 


// $('.datepicker').datepicker({
//   i18n: {
//   months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
//   monthsShort: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
//   weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabádo'],
//   weekdaysShort: ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab'],
//   weekdaysAbbrev: ['D', 'S', 'T', 'Q', 'Q', 'S', 'S'],
//   today: 'Hoje',
//   clear: 'Limpar',
//   cancel: 'Sair',
//   done: 'Confirmar',
//   labelMonthNext: 'Próximo mês',
//   labelMonthPrev: 'Mês anterior',
//   labelMonthSelect: 'Selecione um mês',
//   labelYearSelect: 'Selecione um ano',
//   selectMonths: true,
//   selectYears: 4,
//   },
//   format: 'dd/mm/yyyy',
//   container: 'body',
//   minDate: new Date(),
//   });


  $('.datepicker').datepicker({
    selectMonths: true,
    selectYears: 15,
    // Título dos botões de navegação
    labelMonthNext: 'Próximo Mês',
    labelMonthPrev: 'Mês Anterior',
    // Título dos seletores de mês e ano
    labelMonthSelect: 'Selecione o Mês',
    labelYearSelect: 'Selecione o Ano',
    // Meses e dias da semana
    monthsFull: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
    monthsShort: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    weekdaysFull: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
    weekdaysShort: ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab'],
    // Letras da semana
    weekdaysLetter: ['D', 'S', 'T', 'Q', 'Q', 'S', 'S'],
    //Botões
    today: 'Hoje',
    clear: 'Limpar',
    close: 'Fechar',
    // Formato da data que aparece no input
    format: 'dd/mm/yyyy',
    onClose: function() {
      $(document.activeElement).blur()
    }
  });

