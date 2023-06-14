const result = document.getElementById('result');

let approval = 'Not approved!';

function getApproval() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve('Approved!');
    }, 500);
  });
}

/* 
getApproval().then((resolvedApproval) => {
  result.textContent = resolvedApproval;
});
 */

async function setApprovalText() {
  const approvalPromise = await getApproval();
  result.textContent = approvalPromise;
}

setApprovalText();