export default class FoldableComment {
  constructor(dom){
    this.containerDom = dom;
    this.headerDom = this.containerDom.querySelector('div.user');
    this.contentDom = this.containerDom.querySelector('div.comments__content');
    this.actionDom = this.containerDom.querySelector('div.act');
    this.isFolded = false;
  }

  main() {
    if (!this.checkRequirements()) { return; }

    this.initializeFoldButton();
    this.gatherReplies();
    this.listenToSignal();
  }

  checkRequirements() {
    if (this.headerDom && this.contentDom && this.actionDom) {
      return true;
    }

    return false;
  }

  initializeFoldButton() {
    let foldButton = document.createElement('a');
    foldButton.href = '#';
    foldButton.classList.add('comments__fold-button');
    foldButton.textContent = '[-]';

    this.headerDom.insertBefore(foldButton, this.headerDom.firstChild);
    foldButton.addEventListener('click', this.toggle.bind(this));

    this.foldButton = foldButton;
  }

  gatherReplies() {
    this.commentId = this.containerDom.dataset.commentId;

    const replySelector = `.comments[data-parent-id="${this.commentId}"]`;
    this.replies = document.querySelectorAll(replySelector);
  }

  listenToSignal() {
    this.containerDom.addEventListener('foldable-comment:hide', this.hide.bind(this));
    this.containerDom.addEventListener('foldable-comment:show', this.show.bind(this));
  }

  toggle() {
    if (this.isFolded) {
      this.unfold();
    } else {
      this.fold();
    }
  }

  fold() {
    this.contentDom.style.display = 'none';
    this.actionDom.style.display = 'none';
    this.foldButton.textContent = '[+]';
    this.isFolded = true;

    this.hideAllReplies();
  }

  unfold() {
    this.contentDom.style.display = 'block';
    this.actionDom.style.display = 'block';
    this.foldButton.textContent = '[-]';
    this.isFolded = false;

    this.showAllReplies();
  }

  hide() {
    this.containerDom.style.display = 'none';
    this.hideAllReplies();
  }

  show() {
    this.containerDom.style.display = 'block';
    this.unfold(); //we call unfold instead of just showAllReplies because it will be weird if a comment is folded but its replies is shown
  }

  hideAllReplies() {
    if (this.replies.length) {
      this.sendSignalToReplies('foldable-comment:hide');
    }
  }

  showAllReplies() {
    if (this.replies.length) {
      this.sendSignalToReplies('foldable-comment:show');
    }
  }

  sendSignalToReplies(eventName) {
    Array.prototype.forEach.call(this.replies, (replyDom) => {
      let signal = new Event(eventName);
      replyDom.dispatchEvent(signal);
    });
  };
}
