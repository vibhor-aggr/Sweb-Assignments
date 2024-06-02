import org.apache.jena.rdf.model.*;
import org.apache.jena.reasoner.Reasoner;
//import org.apache.jena.reasoner.ReasonerRegistry;
import org.apache.jena.reasoner.rulesys.GenericRuleReasonerFactory;
import org.apache.jena.riot.RDFDataMgr;
//import org.apache.jena.reasoner.*;
//import org.apache.jena.util.FileManager;
import org.apache.jena.util.PrintUtil;
import org.apache.jena.vocabulary.ReasonerVocabulary;
import java.io.FileWriter;
import java.io.PrintWriter;

public class App {
    public static void main(String[] args) throws Exception {

        Model m = ModelFactory.createDefaultModel();
        Resource configuration =  m.createResource().addProperty(ReasonerVocabulary.PROPsetRDFSLevel, "full");
        configuration.addProperty(ReasonerVocabulary.PROPruleMode, "hybrid");
        configuration.addProperty(ReasonerVocabulary.PROPruleSet,  "C:/Users/Vibhor Aggarwal/Documents/6thSem/CSE632/A1/2021111_Assignment1/Q2/Q2.rules");


        Reasoner reasoner = GenericRuleReasonerFactory.theInstance().create(configuration);

        Model data = RDFDataMgr.loadModel("file:C:/Users/Vibhor Aggarwal/Documents/6thSem/CSE632/A1/2021111_Assignment1/Q1.ttl");
        InfModel infmodel = ModelFactory.createInfModel(reasoner, data);

        StmtIterator i = infmodel.listStatements((Resource)null, (Property)null, (RDFNode)null);
        PrintWriter out = null;
        try{
            out=new PrintWriter(new  FileWriter("C:/Users/Vibhor Aggarwal/Documents/6thSem/CSE632/A1/2021111_Assignment1/Q2/inference.txt"));
            while (i.hasNext()) {
                Statement stmt = i.nextStatement();
                System.out.println(" - " + PrintUtil.print(stmt));
                out.println(" - " + PrintUtil.print(stmt));
            }
        }
        finally{
            if(out!=null){
                out.close();
            }
        }
    }
}
