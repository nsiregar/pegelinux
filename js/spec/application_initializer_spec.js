import ApplicationInitializer from '../src/application_initializer';

describe('ApplicationInitializer', () => {
  describe('.main', () => {
    it('bind events DOMContentLoaded with event listener that executes all necessary initializers', () => {
      spyOn(ApplicationInitializer, 'initializeFoldableComment');
      spyOn(ApplicationInitializer, 'initializeMoment');
      
      ApplicationInitializer.main();

      expect(ApplicationInitializer.initializeFoldableComment).not.toHaveBeenCalled();
      expect(ApplicationInitializer.initializeMoment).not.toHaveBeenCalled();

      document.dispatchEvent(new Event('DOMContentLoaded'));

      expect(ApplicationInitializer.initializeFoldableComment).toHaveBeenCalled();
      expect(ApplicationInitializer.initializeMoment).toHaveBeenCalled();
    });
  });

  describe('.initializeFoldableComment', () => {
    it('find all HTML Nodes with class comments, create and ran FoldableComment instances on them', () => {
      let comment1 = affix('.comments'),
          header1 = comment1.affix('.user'),
          content1 = comment1.affix('.comments__content'),
          action1 = comment1.affix('.act');
          
      let comment2 = affix('.comments'),
          header2 = comment1.affix('.user'),
          content2 = comment1.affix('.comments__content'),
          action2 = comment1.affix('.act');

      ApplicationInitializer.initializeFoldableComment();

      expect(comment1[0]).toContainText('[-]');
    });
  });

  describe('.initializeMoment', () => {
    it('find all HTML Nodes with class flask-moment, ran moment on them', () => {
      let minutes = faker.random.number({ 'min': 2, 'max': 40 });
      let sampleTimestamp = (new Date(Date.now() - (minutes * 60 * 1000))).toISOString();

      let momentables = Array
        .apply(null, { length: 10 })
        .map(_x => affix(`.flask-moment[data-timestamp="${ sampleTimestamp }"][style="display: none"]`));

      ApplicationInitializer.initializeMoment();

      momentables.forEach(momentable => {
        expect(momentable).toContainText(`${ minutes } minutes ago`);
        expect(momentable).toBeVisible();
      });
    });
  });
});
