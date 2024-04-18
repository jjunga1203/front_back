const formTags = document.querySelectorAll('.likes-form')
const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value

formTags.forEach((formTag) => {
    const likeUrl = formTag.action
    formTag.addEventListener('submit', (event) =>{
        event.preventDefault()

        axios({
            method: 'post',
            url : likeUrl,
            headers : {'X-CSRFToken': csrfToken},
            mode: 'same-origin'
        }).then((resp) => {
            responseData = resp.data
            const isLiked = responseData.is_liked
            const reviewId = responseData.review_id
            const likeCnt = responseData.like_cnt
            const likeBtn = document.querySelector(`#like-${reviewId}`)
            const likeCntTag = document.querySelector(`#like_cnt-${reviewId}`)

            // console.log(likeCntTag)

            if(isLiked){
                likeBtn.value = '좋아요 취소'
            }else{
                likeBtn.value = '좋아요'
            }
            likeCntTag.textContent = likeCnt
        }).catch((error) => {
            console.log(error)
        })
    })
    
});