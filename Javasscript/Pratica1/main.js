
$(function(){
    $('h1').css({
        "font-family": "Arial",
        "text-align": 'center',
        'font-size': '55px',
    });
    $('#a').css({
        "background-color": 'blue',
    });
    $('#b').css({
        "background-color":'red',
    })
    $('#c').css({
        "background-color": 'green',
    });
    $('#d').css({
        "background-color":'yellow',
    });
    $('button').click(function getNormal(){
        $('div').css({
                'width':'90px',
                'height':'90px',
            });
        $('button').click(function getBigger(){
            $('div').css({
                'width':'150px',
                'height':'150px',
            });
            $('button').click(function getHide(){
                $('div').css({
                    'width':'0px',
                    'height':'0px',
                })
                $('button').click(function getNormal2(){
                    getNormal()
                })
            })
        });
    });
});