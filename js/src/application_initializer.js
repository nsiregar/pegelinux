import FoldableComment from './foldable_comment';
import moment from 'moment-mini';

export default class ApplicationInitializer {
  static main() {
    document.addEventListener('DOMContentLoaded', () => {
      this.initializeFoldableComment();
      this.initializeMoment();
    });
  }

  static initializeFoldableComment() {
    let commentNodes = document.getElementsByClassName('comments');

    Array.prototype.forEach.call(commentNodes, (commentNode) => {
      let foldableComment = new FoldableComment(commentNode);
      foldableComment.main();
    });
  }

  static initializeMoment() {
    let momentables = document.getElementsByClassName('flask-moment');

    Array.prototype.forEach.call(momentables, (momentable) => {
      this._runMoment(momentable);
    });
  }

  static _runMoment(momentable) {
    let timestamp = momentable.dataset.timestamp;
    let timeAgo = moment(timestamp).fromNow(0);
    momentable.textContent = timeAgo;
    momentable.style.display = '';
  }
}
