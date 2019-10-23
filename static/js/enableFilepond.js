// Script for configuring FilePond, a file upload library.
// See https://github.com/pqina/filepond for more information.

FilePond.setOptions({
    instantUpload: true,
    allowMultiple: false,
    allowReplace: false,
    allowImagePreview: true,
    server: {
      process: '/upload',
      fetch: null,
      revert: null,
      restore: null,
      load: null
    }
  });
  FilePond.registerPlugin(
    FilePondPluginImagePreview
  );
  const pond = FilePond.create(document.querySelector('input[type="file"]'));
  pond.on('processfile', (error, file) => {
    if (error === null) {

      let data = JSON.parse(file.serverId);
      
      let id = data[0];
      let label = data[1];
      console.log(id);
      console.log(label);

      let uploadFileIdInputNode = document.querySelector(`#image`);
      uploadFileIdInputNode.value = id;
      let labelInputNode = document.querySelector(`#label`);
      labelInputNode.value = label;
    }
  })