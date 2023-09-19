

// tinymce.init({
//   selector: '#id_content',
//   images_upload_url: '{% url "blog_app:image_upload" %}',
// });


// const input = document.getElementById('file')
// const output = document.getElementById('output')

// document.getElementById('file').addEventListener('input', (event) => {
//   const files = event.target.files
//   output.textContent = Array.from(files).map(file => file.name).join('\n')
// })
function imageIntoContent(iamge_url){

  var imageFile = CKEDITOR.instances.id_content;
  // 저장된 이미지 주소를 가져와서 img로 보이게 img태그를 붙임
  var value =  "<img src='"+ iamge_url +"'/>";

  // 커서에서 위치잡도록 설정
  if ( imageFile.mode == 'wysiwyg' )
  {
    // 이미지를 ck에 넣어줌
    imageFile.insertHtml( value );
  }
  else
    alert( '업로드경고' );
}
//페이지 작성후 불러오기
// document.addEventListener('DOMContentLoaded', (event) => {

  // 이미지 업로드 후 에디터 내에 이미지 삽입
  document.getElementById('imageUpload').addEventListener('change', function() {
    let formData = new FormData();

    formData.append('file', this.files[0]);

    fetch('{% url "blog_app:image_upload" %}', {
      method: 'POST',
      body: formData,
      headers: {
        'X-CSRFToken': '{{ csrf_token }}'
      }
    })
    .then(response => response.json())
    .then(data => {
      console.log(data.location);
      // ckedit에서 이미지 업로드함수
      console.log(111111)
       imageIntoContent(data.location);
    })
    .catch(error => console.error('Error:', error));
  });





// //이미지 업로드
// tinymce.init({
//   selector: '#content',
//   images_upload_url: '{% url "blog_app:image_upload" %}',
// });
// // // 1. document 이용하여 id값을 불러옴.
// // let imageUpLoad = document.querySelector('#imageUpload')
// // imageUpLoad.addEventListener('change', function() {
// //   // 메모리할당
// //   let formData = new FormData();
// //   formData.append('file', this.files[0]);
// //   console.log(formData);
// //   //promise로 받는다.
// //   fetch('{% url "blog_app:image_upload" %}', {
// //     method: 'POST',
// //     body: formData,
// //     headers: {
// //       'X-CSRFToken': '{{ csrf_token }}'
// //     }
// //   })
// //   .then(response => response.json()) // 다시 제이슨으로 파싱
// //   .then(data => {
// //     tinyMCE.activaEditor.insertContent(`<img src="${data.location}"/>`);
// //   })
// //   .catch(error => console.log('ERROR', error));
// // });