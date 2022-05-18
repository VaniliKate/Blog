$(document).ready(()=>{
    
    console.log(upvoted)
    if (upvoted == 'True'){
        $('#pitch-up').addClass('pitch-up')
    }
    else{
        $('#pitch-up').removeClass('pitch-up')
    }
    if (downvoted == 'True'){
        $('#pitch-down').addClass('pitch-down')
    }
    else{
        $('#pitch-down').removeClass('pitch-down')
    }
    
    $('#pitch-up').click(()=>{
       $.getJSON('/upvote_pitch', {
            action_perform: 'up_vote',
            pitch_id: pitch_id
          }, (data)=> {
              if( data.auth === true){
                if (data.upvote === true ){
                    $('#pitch-up').addClass('pitch-up')
                    $('.up-counter').text(data.upvotes)
                    if(data.downvotechange){
                        $('#pitch-down').removeClass('pitch-down')
                        $('.down-counter').text(data.downvotes)
                    }
                }else if (data.upvote === false){
                    $('#pitch-up').removeClass('pitch-up')
                    $('#pitch-down').removeClass('pitch-down')
                    $('.up-counter').text(data.upvotes)
                    $('.down-counter').text(data.downvotes)
                }
              }else{
                  console.log(data.auth)
                  $('.action-not-performed-error').show()
              }
            
          });
          return false;
        });

        $('#pitch-down').click(()=>{
            $.getJSON('/downvote_pitch', {
                 action_perform: 'down_vote',
                 pitch_id: pitch_id
               }, (data)=> {
                   if( data.auth === true){
                     if (data.downvote === true ){
                         if (data.upvotechange){
                            $('#pitch-up').removeClass('pitch-up')
                            $('.up-counter').text(data.upvotes)
                         }
                         $('#pitch-down').addClass('pitch-down')
                         $('.down-counter').text(data.downvotes)
                     }else if (data.downvote === false){
                         $('#pitch-down').removeClass('pitch-down')
                         $('.down-counter').text(data.downvotes)
                     }
                   }else{
                       $('.action-not-performed-error').show()
                   }
                 
               });
               return false;
             });
        $('#comment_form').submit(function(e){
            comment = $("#comment-box").val()
            $("#comment-box").val('')
            e.preventDefault();
            $.ajax({
                url:`/comment/${pitch_id}`,
                type:'post',
                data: {comment: comment},
                success:function(data){
                    if( data.auth ===true ){
                        $('.comments-count').text(data.comments_count)
                        $('.all-comments').append(
                            `<div class="row">
                            <div class=" col-12 col-sm-6 pitch card mb-3">
                                <div class="row pt-4 pl-4">
                                    <div class="col-2 col-sm-1">
                                        <span class="material-icons pitch-img">account_circle</span>
                                    </div>
                                    <div class="col pitch-owner">
                                         ${data.comment_f_name} ${data.comment_l_name}
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col pitch-message">
                                        ${data.comment_message}
                                    </div>
                                </div>
                                <div class="row thumbs pb-4">
                                    <div class="col-3 col-sm-2">
                                        <span class="material-icons" id="pitch-up">thumb_up_alt</span>
                                        <div class="row">
                                            <div class="col up-counter">
                                                 0 
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-3 col-sm-2 thumb">
                                        <span class="material-icons" id="pitch-down">thumb_down_alt</span>
                                        <div class="row">
                                            <div class="col down-counter">
                                                0
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-3 col-sm-2 thumb">
                                        <span class="material-icons" id="pitch-down">comment</span>
                                        <div class="row">
                                            <div class="col down-counter">
                                                0
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>`
                        )
                    }else{
                        $('.action-not-performed-error').show()
                    }
                    
                }
            });
        });
})
