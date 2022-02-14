
$(document).ready(function(){

   
    //Carregar os Formulários
    $('#div_id_grupo').addClass('col-md-4');
    $('#div_id_projeto').addClass('col-md-4');
    $('#div_id_cliente').addClass('col-md-4');
    $('#div_id_n_de_part').addClass('col-md-4');
    $('#div_id_descricao').addClass('col-md-4');
    $('#div_id_tutorial').addClass('col-md-12');
    $('#div_id_ver').addClass('col-md-4');
    $('#div_id_status').addClass('col-md-4');
    $('#div_id_dataIni').addClass('col-md-4');
    $('#div_id_dataFim').addClass('col-md-4');
    $('span:contains("*")').css('color', 'red');

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
