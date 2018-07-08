import FoldableComment from './foldable_comment';

document.addEventListener('DOMContentLoaded', () => {
  'use strict';

  let commentNodes = document.getElementsByClassName('comments');

  Array.prototype.forEach.call(commentNodes, (commentNode) => {
    let foldableComment = new FoldableComment(commentNode);
    foldableComment.main();
  });
});
