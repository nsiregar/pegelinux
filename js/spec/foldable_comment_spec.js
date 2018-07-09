import FoldableComment from '../src/foldable_comment';

describe('FoldableComment', () => {
  let foldableComment;
  let $commentDom, commentDom, $headerDom, headerDom, $contentDom, contentDom, $actionDom, actionDom;

  beforeEach(() => {
    $commentDom = affix('.comments[data-comment-id=123]');
    $headerDom  = $commentDom.affix('.user');
    $contentDom = $commentDom.affix('.comments__content');
    $actionDom  = $commentDom.affix('.act');

    commentDom = $commentDom[0];
    headerDom  = $headerDom[0];
    contentDom = $contentDom[0];
    actionDom  = $actionDom[0];

    foldableComment = new FoldableComment(commentDom);
  });

  describe('#constructor', () => {
    it('takes argument, the DOM and storing it to attribute', () => {
      expect(foldableComment.containerDom).toEqual(commentDom);
    });

    it('have attribute isFolded with initial value false', () => {
      expect(foldableComment.isFolded).toEqual(false);
    });

    it('looks for main child element required: div.user, div.comment__content, div.act and store it to attribute', () => {
      expect(foldableComment.headerDom).toEqual(headerDom);
      expect(foldableComment.contentDom).toEqual(contentDom);
      expect(foldableComment.actionDom).toEqual(actionDom);
    });
  });

  describe('#main', () => {
    let spyCheckRequirements;

    beforeEach(() => {
      spyCheckRequirements = spyOn(foldableComment, 'checkRequirements');
      spyOn(foldableComment, 'initializeFoldButton');
      spyOn(foldableComment, 'gatherReplies');
      spyOn(foldableComment, 'listenToSignal');
    });

    describe('requirements satisfied', () => {
      it('calls initializeFoldButton, gatherReplies, and listenToSignal', () => {
        spyCheckRequirements.and.returnValue(true)
        foldableComment.main();

        expect(foldableComment.initializeFoldButton).toHaveBeenCalled();
        expect(foldableComment.gatherReplies).toHaveBeenCalled();
        expect(foldableComment.listenToSignal).toHaveBeenCalled();
      });
    });

    describe('requirements not satisfied', () => {
      it('doesnt call initializeFoldButton, gatherReplies, nor listenToSignal', () => {
        spyCheckRequirements.and.returnValue(false)
        foldableComment.main();

        expect(foldableComment.initializeFoldButton).not.toHaveBeenCalled();
        expect(foldableComment.gatherReplies).not.toHaveBeenCalled();
        expect(foldableComment.listenToSignal).not.toHaveBeenCalled();
      });
    });
  });

  describe('#checkRequirements', () => {
    describe('when headerDom, contentDom, and actionDom is available', () => {
      it('returns true', () => {
        expect(foldableComment.checkRequirements()).toBe(true);
      });
    });

    describe('no headerDom', () => {
      it('returns false', () => {
        foldableComment.headerDom = null;
        expect(foldableComment.checkRequirements()).toBe(false);
      });
    });

    describe('no contentDom', () => {
      it('returns false', () => {
        foldableComment.contentDom = null;
        expect(foldableComment.checkRequirements()).toBe(false);
      });
    });

    describe('no actionDom', () => {
      it('returns false', () => {
        foldableComment.actionDom = null;
        expect(foldableComment.checkRequirements()).toBe(false);
      });
    });
  });

  describe('#initializeFoldButton', () => {
    beforeEach(() => {
      spyOn(foldableComment, 'toggle');
    });

    it('insert span with content "[-]" to headerDom before its content, also store its dom to this.foldButton', () => {
      headerDom.textContent = 'some name...'
      foldableComment.initializeFoldButton();
      expect(headerDom).toHaveText('[-]some name...');

      let createdButton = headerDom.querySelector('a.comments__fold-button');
      expect(createdButton).toEqual(foldableComment.foldButton);
    });

    it('binds event click to foldButton with function this.fold as listener', () => {
      foldableComment.initializeFoldButton();

      expect(foldableComment.toggle).not.toHaveBeenCalled();
      foldableComment.foldButton.dispatchEvent(new Event('click'));
      expect(foldableComment.toggle).toHaveBeenCalled();
    });
  });

  describe('#listenToSignal', () => {
    it('binds event foldable-comment:hide to containerDom, with method #hide as listener', () => {
      spyOn(foldableComment, 'hide');
      foldableComment.listenToSignal();

      let signal = new Event('foldable-comment:hide');

      commentDom.dispatchEvent(signal);
      expect(foldableComment.hide).toHaveBeenCalled();      
    });

    it('binds event foldable-comment:show to containerDom, with method #show as listener', () => {
      spyOn(foldableComment, 'show');
      foldableComment.listenToSignal();

      let signal = new Event('foldable-comment:show');

      commentDom.dispatchEvent(signal);
      expect(foldableComment.show).toHaveBeenCalled();      
    });
  });

  describe('#toggle', () => {
    beforeEach(() => {
      spyOn(foldableComment, 'fold');
      spyOn(foldableComment, 'unfold');
    });

    describe('when isFolded is false', () => {
      it('calls method fold()', () => {
        foldableComment.isFolded = false;

        foldableComment.toggle();

        expect(foldableComment.fold).toHaveBeenCalled();
        expect(foldableComment.unfold).not.toHaveBeenCalled();
      });
    });

    describe('when isFolded is true', () => {
      it('calls method unfold()', () => {
        foldableComment.isFolded = true

        foldableComment.toggle();

        expect(foldableComment.fold).not.toHaveBeenCalled();
        expect(foldableComment.unfold).toHaveBeenCalled();
      });
    });
  });

  describe('#fold', () => {
    let dummyButton;

    beforeEach(() => {
      dummyButton = affix('div')[0];
      foldableComment.foldButton = dummyButton;
      spyOn(foldableComment, 'hideAllReplies');
    });

    it('set css display none to contentDom and actionDom', () => {
      contentDom.style.display = 'block';
      actionDom.style.display = 'block';

      foldableComment.fold();

      expect(contentDom).not.toBeVisible();
      expect(actionDom).not.toBeVisible();
    });

    it('set foldButton textContent to `[+]`', () => {
      foldableComment.fold();
      expect(dummyButton).toHaveText('[+]');
    });

    it('set attribute isFolded to true', () => {
      foldableComment.isFolded = false;
      foldableComment.fold();
      expect(foldableComment.isFolded).toBe(true);
    });

    it('calls #hideAllReplies', () => {
      foldableComment.fold();
      expect(foldableComment.hideAllReplies).toHaveBeenCalled();
    });
  });

  describe('#unfold', () => {
    let dummyButton;

    beforeEach(() => {
      dummyButton = affix('div')[0];
      foldableComment.foldButton = dummyButton;
      spyOn(foldableComment, 'showAllReplies');
    });

    it('set css display block to contentDom and actionDom', () => {
      contentDom.style.display = 'none';
      actionDom.style.display = 'none';

      foldableComment.unfold();

      expect(contentDom).toBeVisible();
      expect(actionDom).toBeVisible();
    });

    it('set foldButton textContent to `[-]`', () => {
      foldableComment.unfold();
      expect(dummyButton).toHaveText('[-]');
    });

    it('set attribute isFolded to false', () => {
      foldableComment.isFolded = true;
      foldableComment.unfold();
      expect(foldableComment.isFolded).toBe(false);
    });

    it('calls #showAllReplies', () => {
      foldableComment.unfold();
      expect(foldableComment.showAllReplies).toHaveBeenCalled();
    });
  });

  describe('#hide', () => {
    it('hides containerDom and calls #hideAllReplies', () => {
      spyOn(foldableComment, 'hideAllReplies');
      foldableComment.containerDom.style.display = 'block';

      foldableComment.hide();

      expect(foldableComment.containerDom).not.toBeVisible();
      expect(foldableComment.hideAllReplies).toHaveBeenCalled();
    });
  });

  describe('#show', () => {
    it('show containerDom and calls #unfold', () => {
      spyOn(foldableComment, 'unfold');
      foldableComment.containerDom.style.display = 'none';

      foldableComment.show();

      expect(foldableComment.containerDom).toBeVisible();
      expect(foldableComment.unfold).toHaveBeenCalled();
    })
  });

  describe('#gatherReplies', () => {
    it('takes DOM attribute data-comment-id and store its value to commentId', () => {
      foldableComment.gatherReplies();
      expect(foldableComment.commentId).toEqual('123');
    });

    it('gather other comments that have attribute data-parent-id of this commentId, storing them to childCommentDoms', () => {
      let $child1 = affix('.comments[data-parent-id=123]'),
          $child2 = affix('.comments[data-parent-id=123]'),
          $notChild1 = affix('.comments[data-parent-id=456]'),
          $notChild2 = affix('.not-comments[data-parent-id=123]');

      let child1 = $child1[0],
          child2 = $child2[0],
          notChild1 = $notChild1[0],
          notChild2 = $notChild2[0];

      foldableComment.gatherReplies();
      expect(foldableComment.replies).toContain(child1);
      expect(foldableComment.replies).toContain(child2);
      expect(foldableComment.replies).not.toContain(notChild1);
      expect(foldableComment.replies).not.toContain(notChild2);
    });
  });

  describe('#hideAllReplies', () => {
    describe('when #replies exists', () => {
      it('call #sendSignalToReplies with params foldable-comment:hide', () => {
        affix('.dummyreplies');
        let replies = document.querySelectorAll('.dummyreplies');
        foldableComment.replies = replies;

        spyOn(foldableComment, 'sendSignalToReplies');

        foldableComment.hideAllReplies();

        expect(foldableComment.sendSignalToReplies).toHaveBeenCalledWith('foldable-comment:hide');
      });
    });

    describe('when #replies doesnt exists', () => {
      it('doesnt call #sendSignalToReplies', () => {
        let replies = document.querySelectorAll('.nosuchthings');
        foldableComment.replies = replies;

        spyOn(foldableComment, 'sendSignalToReplies');

        foldableComment.hideAllReplies();

        expect(foldableComment.sendSignalToReplies).not.toHaveBeenCalled();
      });
    });
  });

  describe('#showAllReplies', () => {
    describe('when #replies exists', () => {
      it('call #sendSignalToReplies with params foldable-comment:hide', () => {
        affix('.dummyreplies');
        let replies = document.querySelectorAll('.dummyreplies');
        foldableComment.replies = replies;

        spyOn(foldableComment, 'sendSignalToReplies');

        foldableComment.showAllReplies();

        expect(foldableComment.sendSignalToReplies).toHaveBeenCalledWith('foldable-comment:show');
      });
    });

    describe('when #replies doesnt exists', () => {
      it('doesnt call #sendSignalToReplies', () => {
        let replies = document.querySelectorAll('.nosuchthings');
        foldableComment.replies = replies;

        spyOn(foldableComment, 'sendSignalToReplies');

        foldableComment.showAllReplies();

        expect(foldableComment.sendSignalToReplies).not.toHaveBeenCalled();
      });
    });
  });

  describe('sendSignalToReplies', () => {
    it('send event foldable-comment:toggle-hide-show to all DOM replies', () => {
      let $child1 = affix('.dummyreplies'),
          $child2 = affix('.dummyreplies');

      let child1 = $child1[0],
          child2 = $child2[0];

      let replies = document.querySelectorAll('.dummyreplies');

      foldableComment.replies = replies;

      let listener1 = jasmine.createSpy('event listener for child1'),
          listener2 = jasmine.createSpy('event listener for child2');

      child1.addEventListener('dummyEvent1', listener1);
      child2.addEventListener('dummyEvent2', listener2);

      foldableComment.sendSignalToReplies('dummyEvent1');
      expect(listener1).toHaveBeenCalled();

      foldableComment.sendSignalToReplies('dummyEvent2');
      expect(listener2).toHaveBeenCalled();
    });
  });
});
