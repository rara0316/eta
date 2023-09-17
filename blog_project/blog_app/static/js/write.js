//이미지 업로드
tinymce.init({
  selector: '#content',
  images_upload_url: '{% url "blog_app:image_upload" %}',
});

// 1. document 이용하여 id값을 불러옴.
let imageUpLoad = document.querySelector('#imageUpload')
imageUpLoad.addEventListener('change', function() {
  // 메모리할당
  let formData = new FormData();
  formData.append('file', this.files[0]);
  console.log(formData);
  //promise로 받는다.
  fetch('{% url "blog_app:image_upload" %}', {
    method: 'POST',
    body: formData,
    headers: {
      'X-CSRFToken': '{{ csrf_token }}'
    }
  })
  .then(response => response.json()) // 다시 제이슨으로 파싱
  .then(data => {
    tinyMCE.activaEditor.insertContent(`<img src="${data.location}"/>`);
  })
  .catch(error => console.log('ERROR', error));
});