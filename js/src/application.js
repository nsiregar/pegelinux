import FoldableComment from './foldable_comment';

document.addEventListener('DOMContentLoaded', () => {
  let commentNodes = document.getElementsByClassName('comments');

  Array.prototype.forEach.call(commentNodes, (commentNode) => {
    let foldableComment = new FoldableComment(commentNode);
    foldableComment.main();
  });
});
