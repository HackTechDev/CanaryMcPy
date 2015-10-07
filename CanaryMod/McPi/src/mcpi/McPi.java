/***
 ***/
package mcpi;//(1)
import net.canarymod.plugin.Plugin;//(2)
import net.canarymod.logger.Logman;
import net.canarymod.Canary;
import net.canarymod.commandsys.*;
import net.canarymod.chat.MessageReceiver;
import java.io.*;
import java.io.IOException;
import java.io.InputStream;
import java.util.*;

public class McPi extends Plugin implements CommandListener {//(3)

	public static Logman logger;

	public McPi() { 
		logger = getLogman();
	}

	@Override
		public boolean enable() { 
			logger.info("Starting up");   
			try {
				Canary.commands().registerCommands(this, this, false);
			} catch (CommandDependencyException e) {
				logger.error("Duplicate command name");
			}
			return true;
		}

	@Override
		public void disable() {
		}

	@Command(aliases = { "mcpi" },//(4)
			description = "Execute Python command",
			permissions = { "" },
			toolTip = "/mcpi")

		public void helloCommand(MessageReceiver caller, String[] parameters) throws IOException
		{
			try {
				//String cmd = "ls -al";
				String cmd = "./McPi/mcpi.py";

				Runtime run = Runtime.getRuntime();
				Process pr = run.exec(cmd);
				pr.waitFor();

				BufferedReader buf = new BufferedReader(new InputStreamReader(pr.getInputStream()));

				String line = "";
				while ((line=buf.readLine())!=null) {
					System.out.println(line);
				}
			} catch (Exception ex) {
   				ex.printStackTrace();
   			}

			String msg = "Call McPi";
			Canary.instance().getServer().broadcastMessage(msg);
		}

}
