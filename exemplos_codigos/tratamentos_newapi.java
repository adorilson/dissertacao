// EC direta

public method(){

    if (VERSION.SDK_INT>11){
        ocorrencia_newapi_ou_inlineapi()
    }

}

//  variação de EC direta

public method(){

    if (VERSION.SDK_INT<=11){
        return
    }

    ocorrencia_newapi_ou_inlineapi()
}


// EC indireta
public method(){
    
    if (VERSION.SDK_INT>11){
        method_A()
    } 

}

private method_A(){
        ocorrencia_newapi_ou_inlineapi()
}


// tratamento de exceção

try{
    ocorrencia_newapi_ou_inlineapi()
}catch(Exception e){
    // some code...
}

public abstract class AbstracClass {
    private static AbstractClass concret;

    public abstract action();

    public static templatMethod() {
        if (Build.VERSION.SDK_INT < 11) {
                concret = new ConcretClass1();
            } else
                concret = new ConcretClass2();
        }

        concret.action();
    }
}


public class ConcretClass2 extends AbstractClass {

    public abstract action(){
        ocorrencia_newapi_ou_inlineapi()
    }    
}

public class PreferenceWithHeaders extends PreferenceActivity {
        
    public void onBuildHeaders(List<Header> target) {
        ocorrencia_newapi_ou_inlineapi()
    }

}



public class PrefsBackupAgent extends BackupAgentHelper {
    ...
}

<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <application
        android:backupAgent="PrefsBackupAgent"/>
</manifest>



// method_A() não chamado em lugar algum
method_A(){
        ocorrencia_newapi_ou_inlineapi()
}


