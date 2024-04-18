const formElement = document.querySelector('#follow-form')
const followUrl = formElement.action
const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value

const submitFormHandler = (event) => {
    event.preventDefault()
    // console.log(csrfToken)

    axios({
        method: 'post',
        url: followUrl,
        headers: {'X-CSRFToken': csrfToken}
    }).then((resp) => {
        const submitElement = document.querySelector('#submit-input')
        const followerCntElement = document.querySelector('#follower-cnt')
        const followingCntElement = document.querySelector('#following-cnt')
    
        const responseData = resp.data
        const isFollowed = responseData.is_followed
        const followerCnt = responseData.follower_cnt
        const followingCnt = responseData.following_cnt

        followerCntElement.textContent = followerCnt
        followingCntElement.textContent = followingCnt

        if(isFollowed){
            submitElement.value = '언팔로우'
        }else{
            submitElement.value = '팔로우'
        }
        // console.log(resp)
    }).catch((error) => {
        console.log(error)
    })
}

formElement.addEventListener('submit', submitFormHandler)