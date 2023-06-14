// Get DOM elements
const generateButton = document.getElementById('generate-button');
const postTitle = document.getElementById('post-title');
const postId = document.getElementById('post-id');
const postContent = document.getElementById('post-content');

// API URL
const api = 'https://us-central1-open-classrooms-js-for-the-web.cloudfunctions.net/widgets';

// A blog about cats
function makeRequest(verb, URL, data) {
  return Promise((resolve, reject) => {
    if (verb === 'POST' && !data) {
      reject({error: 'No data object provided for POST request!'})
    }
    if (verb != 'POST' && verb != 'GET') {
      reject ({error: 'Invalid request VERB!'})
    }

    let request = new XMLHttpRequest();
    request.open(verb, URL);
    request.onreadystatechange = () => {
      if (request.readyState === 4) {
        if (request.status === 200 || request.status === 201) {
          resolve(JSON.parse(request.response));
        } else {
          reject(JSON.parse(request.response));
        }
      }
    }
    if (verb === 'POST') {
      request.setRequestHeader('Content-Type', 'application/json');
      request.send(JSON.stringify(data));
    } else {
      request.send();
    }
  });
}

async function createPost () {
  const uidPromise = makeRequest('GET', api + '/generate-uid');
  const titlePromise = makeRequest('GET', api + '/generate-title');
  const contentPromise = makeRequest('GET', api + '/generate-lorem');
  
  try {
    const [uidRespond, titleRespond, contentRespond] = await Promise.all([uidPromise, titlePromise, contentPromise]);

    const postPromise = makeRequest('POST', api + '/create-post-with-uid', {
      uid: uidRespond.uid,
      title: titleRespond.title,
      content: contentRespond.lorem
    })
    
    try {
      const postReponse = await postPromise;
  
      postId.textContent = postReponse.post.id;
      postTitle.textContent = postReponse.post.title;
      postContent.textContent = postReponse.post.content;  
    } catch (error) {
      postTitle.textContent = error.error;
    }

  } catch (error) {
    postTitle.textContent = error.error;
  }
}

generateButton.addEventListener('click', () => {
  createPost();
})