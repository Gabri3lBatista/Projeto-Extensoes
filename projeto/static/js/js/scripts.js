
$(document).ready(function(){

   $('.form-group').addClass('col-md-4');
   $('#div_id_tutorial').addClass('col-md-12');
   $('.asteriskField').css('color', 'red')
   $('label').css('color', 'black')
   $('#id_dataIni, #id_dataFim').attr('type', 'date');
  $('#div_id_observacao').addClass('col-md-8');


   
    //Carregar os Formulários
   
    var table = $('#dataListagens').DataTable({
        lengthChange: false,
        fixedColumns: false,
        "scrollX": true,
        buttons:[ 'copy', 'excel', 'print', 'pdf' ]
    });
    table.buttons().container()
        .appendTo('#dataListagens_wrapper .col-md-6:eq(0)'
    );
    $('#myInput').on( 'keyup', function () {
        table.search( this.value ).draw();
    } );

    $('.dt-buttons ').addClass("m-0");

    $('#dataListagens_filter').remove();
    
    $('.buttons-copy').attr("class", "buttons-copy btn btn-outline-dark");
    $('.buttons-pdf').attr("class", "buttons-pdf btn btn-outline-dark");
    $('.buttons-excel').attr("class", "buttons-excel btn btn-outline-dark");
    $('.buttons-print').attr("class", "buttons-print btn btn-outline-dark");

    $('button.buttons-copy > span').html("<i class='far fa-copy'></i> Copiar");
    $('button.buttons-pdf > span').html("<i class='far fa-file-pdf'></i> PDF");
    $('button.buttons-excel > span').html("<i class='far fa-file-excel'></i> Excel");
    $('button.buttons-print > span').html("<i class='fas fa-print'></i> Imprimir"); 

    $('[data-toggle="tooltip"]').tooltip();

    $('#myModal').on('shown.bs.modal', function () {
        $('#myInput').trigger('focus')
      })

    
});        
