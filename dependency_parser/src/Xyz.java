import java.util.Arrays;
import java.util.Collection;
import java.util.List;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.StringReader;

import edu.stanford.nlp.process.Tokenizer;
import edu.stanford.nlp.process.TokenizerFactory;
import edu.stanford.nlp.process.CoreLabelTokenFactory;
import edu.stanford.nlp.process.DocumentPreprocessor;
import edu.stanford.nlp.process.PTBTokenizer;
import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.ling.HasWord;
import edu.stanford.nlp.ling.Sentence;
import edu.stanford.nlp.trees.*;
import edu.stanford.nlp.parser.lexparser.LexicalizedParser;

class ParserDemo {
  public static void main(String[] args) {
    String parserModel = "edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz";
    if (args.length > 0) {
      parserModel = args[0];
    }
    LexicalizedParser lp = LexicalizedParser.loadModel(parserModel);

    if (args.length == 0) {
      demoAPI(lp);
    } else {
      String textFile = (args.length > 1) ? args[1] : args[0];
      demoDP(lp, textFile);
    }
  }
  public static void demoDP(LexicalizedParser lp, String filename) {
    // This option shows loading, sentence-segmenting and tokenizing
    // a file using DocumentPreprocessor.
    TreebankLanguagePack tlp = lp.treebankLanguagePack(); // a PennTreebankLanguagePack for English
    GrammaticalStructureFactory gsf = null;
    if (tlp.supportsGrammaticalStructures()) {
      gsf = tlp.grammaticalStructureFactory();
    }
    // You could also create a tokenizer here (as below) and pass it
    // to DocumentPreprocessor
    for (List<HasWord> sentence : new DocumentPreprocessor(filename)) {
      Tree parse = lp.apply(sentence);
      parse.pennPrint();
      System.out.println();

      if (gsf != null) {
        GrammaticalStructure gs = gsf.newGrammaticalStructure(parse);
        Collection tdl = gs.typedDependenciesCCprocessed();
        System.out.println(tdl);
        System.out.println();
      }
    }
  }

  /**
   * demoAPI demonstrates other ways of calling the parser with
   * already tokenized text, or in some cases, raw text that needs to
   * be tokenized as a single sentence.  Output is handled with a
   * TreePrint object.  Note that the options used when creating the
   * TreePrint can determine what results to print out.  Once again,
   * one can capture the output by passing a PrintWriter to
   * TreePrint.printTree. This code is for English.
   */
  public static void demoAPI(LexicalizedParser lp) {
    // This option shows parsing a list of correctly tokenized words
	  
    String[] sent = { "This", "is", "an", "easy", "sentence", "." };
    List<CoreLabel> rawWords = Sentence.toCoreLabelList(sent);
    Tree parse = lp.apply(rawWords);
    parse.pennPrint();
    System.out.println();
    String csvFile = "Testf.csv";
    String csvFile1 = "TestOutPut.csv";
    String line = "";
    String cvsSplitBy = ",";

    try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {
    	FileWriter writer = new FileWriter(csvFile1);

        while ((line = br.readLine()) != null) {

            // use comma as separator
        	System.out.println(line);
            String[] country = line.split(cvsSplitBy);

            String sent2 =country[4];
            TokenizerFactory<CoreLabel> tokenizerFactory =
                PTBTokenizer.factory(new CoreLabelTokenFactory(), "");
            Tokenizer<CoreLabel> tok =
                tokenizerFactory.getTokenizer(new StringReader(sent2));
            List<CoreLabel> rawWords2 = tok.tokenize();
            parse = lp.apply(rawWords2);

            TreebankLanguagePack tlp = lp.treebankLanguagePack(); // PennTreebankLanguagePack for English
            GrammaticalStructureFactory gsf = tlp.grammaticalStructureFactory();
            GrammaticalStructure gs = gsf.newGrammaticalStructure(parse);
            List<TypedDependency> tdl = gs.typedDependenciesCCprocessed();
            for(int i=0;i<tdl.size();i++){
            	if(tdl.get(i).toString().contains("root")){
            		String str=tdl.get(i).toString().substring(13,tdl.get(i).toString().length()-3);
            	        


            	        //custom separator + quote
            	        CSVUtils.writeLine(writer, Arrays.asList(country[0], country[1], country[2],country[3],country[4],str), ',', '"');


            	        
            	}
            }

        }
        writer.flush();
        writer.close();

    } catch (IOException e) {
        e.printStackTrace();
    }

    // This option shows loading and using an explicit tokenizer
    

    // You can also use a TreePrint object to print trees and dependencies
    //TreePrint tp = new TreePrint("penn,typedDependenciesCollapsed");
    //tp.printTree(parse);
  }

  private ParserDemo() {} // static methods only

}
