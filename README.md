<h1 class="gap">0x00. AirBnB clone - The console</h1>


<h4 class="task">
    0. README, AUTHORS
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><ul>
<li>Write a <code>README.md</code>:

<ul>
<li>description of the project</li>
<li>description of the command interpreter:

<ul>
<li>how to start it</li>
<li>how to use it</li>
<li>examples</li>
</ul></li>
</ul></li>
<li>You should have an <code>AUTHORS</code> file at the root of your repository, listing all individuals having contributed content to the repository. Format, see <a href="https://github.com/docker/docker/blob/master/AUTHORS">Docker</a></li>
</ul>


<h4 class="task">
    1. Be PEP8 compliant!
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a beautiful code that passes the PEP8 checks</p>


<h4 class="task">
    2. Unittests
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>All your files, classes, functions must be tested with unit tests</p><p>Tips for testing the console: <a href="http://stackoverflow.com/questions/30056986/create-automated-tests-for-interactive-shell-based-on-pythons-cmd-module">Mock test to redirect stdin/stdout</a></p>


<h4 class="task">
    3. BaseModel
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a class <code>BaseModel</code> that defines all common attributes/methods for other classes:</p><ul>
<li><code>models/base_model.py</code></li>
<li>Public instance attributes: 

<ul>
<li><code>id</code>: string - assign with an <code>uuid</code> when an instance is created:

<ul>
<li>you can use <code>uuid.uuid4()</code> to generate unique <code>id</code> but don't forget to convert to a string</li>
<li>the goal is to have unique <code>id</code> for each <code>BaseModel</code></li>
</ul></li>
<li><code>created_at</code>: datetime - assign with the current datetime when an instance is created</li>
<li><code>updated_at</code>: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object</li>
</ul></li>
<li><code>__str__</code>: should print: <code>[&lt;class name&gt;] (&lt;self.id&gt;) &lt;self.__dict__&gt;</code></li>
<li>Public instance methods:

<ul>
<li><code>save(self)</code>: updates the public instance attribute <code>updated_at</code> with the current datetime</li>
<li><code>to_dict(self)</code>: returns a dictionary containing all keys/values of <code>__dict__</code> of the instance:

<ul>
<li>a key <code>__class__</code> must be added to this dictionary with the class name of the object</li>
<li><code>created_at</code> and <code>updated_at</code> must be converted to string object in ISO format:

<ul>
<li>format: <code>%Y-%m-%dT%H:%M:%S.%f</code> (ex: <code>2017-06-14T22:31:03.285259</code>) </li>
<li>you can use <code>isoformat()</code> of <code>datetime</code> object</li>
</ul></li>
<li>This method will be the first piece of the serialization/deserialization process: create a dictionary representation with "simple object type" of our <code>BaseModel</code></li>
</ul></li>
</ul></li>
</ul>


<h4 class="task">
    4. Create BaseModel from dictionary
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Previously we create a method to generate a dictionary representation of an instance (method <code>to_dict()</code>).</p><p>Now it's time to re-create an instance with this dictionary representation.</p>


<h4 class="task">
    5. Store first object
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Now we can recreate a <code>BaseModel</code> from another one by using a dictionary representation:</p>


<h4 class="task">
    6. Console 0.0.1
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a program called <code>console.py</code> that contains the entry point of the command interpreter:</p><ul>
<li>You must use the module <code>cmd</code></li>
<li>Your class definition must be: <code>class HBNBCommand(cmd.Cmd):</code></li>
<li>Your command interpreter should implement:

<ul>
<li><code>quit</code> and <code>EOF</code> to exit the program</li>
<li><code>help</code> (this action is provided by default by <code>cmd</code> but you should keep it updated and documented)</li>
<li>a custom prompt: <code>(hbnb)</code></li>
<li>an empty line + <code>ENTER</code> shouldn't execute anything</li>
</ul></li>
<li>Your code should not be executed when imported</li>
</ul>


<h4 class="task">
    7. Console 0.1
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Update your command interpreter (<code>console.py</code>) to have these commands:</p><ul>
<li><code>create</code>: Creates a new instance of <code>BaseModel</code>, saves it (to the JSON file) and prints the <code>id</code>. Ex: <code>$ create BaseModel</code>
<ul>
<li>If the class name is missing, print <code>** class name missing **</code> (ex: <code>$ create</code>)</li>
<li>If the class name doesn't exist, print <code>** class doesn't exist **</code> (ex: <code>$ create MyModel</code>)</li>
</ul></li>
<li><code>show</code>: Prints the string representation of an instance based on the class name and <code>id</code>. Ex: <code>$ show BaseModel 1234-1234-1234</code>.

<ul>
<li>If the class name is missing, print <code>** class name missing **</code> (ex: <code>$ show</code>)</li>
<li>If the class name doesn't exist, print <code>** class doesn't exist **</code> (ex: <code>$ show MyModel</code>)</li>
<li>If the <code>id</code> is missing, print <code>** instance id missing **</code> (ex: <code>$ show BaseModel</code>)</li>
<li>If the instance of the class name doesn't exist for the <code>id</code>, print <code>** no instance found **</code> (ex: <code>$ show BaseModel 121212</code>)</li>
</ul></li>
<li><code>destroy</code>: Deletes an instance based on the class name and <code>id</code> (save the change into the JSON file). Ex: <code>$ destroy BaseModel 1234-1234-1234</code>.

<ul>
<li>If the class name is missing, print <code>** class name missing **</code> (ex: <code>$ destroy</code>)</li>
<li>If the class name doesn't exist, print <code>** class doesn't exist ** (ex:</code>$ destroy MyModel<code>)</code></li>
<li>If the <code>id</code> is missing, print <code>** instance id missing **</code> (ex: <code>$ destroy BaseModel</code>)</li>
<li>If the instance of the class name doesn't exist for the <code>id</code>, print <code>** no instance found **</code> (ex: <code>$ destroy BaseModel 121212</code>)</li>
</ul></li>
<li><code>all</code>: Prints all string representation of all instances based or not on the class name. Ex: <code>$ all BaseModel</code> or <code>$ all</code>.

<ul>
<li>If the class name doesn't exist, print <code>** class doesn't exist **</code> (ex: <code>$ all MyModel</code>)</li>
</ul></li>
<li><code>update</code>: Updates an instance based on the class name and <code>id</code> by adding or updating attribute (save the change into the JSON file). Ex: <code>$ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"</code>.

<ul>
<li>Usage: <code>update &lt;class name&gt; &lt;id&gt; &lt;attribute name&gt; "&lt;attribute value&gt;"</code></li>
<li>Only one attribute can be updated at the time</li>
<li>The attribute value must be casted to the attribute type </li>
<li>If the class name is missing, print <code>** class name missing **</code> (ex: <code>$ update</code>)</li>
<li>If the class name doesn't exist, print <code>** class doesn't exist **</code> (ex: <code>$ update MyModel</code>)</li>
<li>If the <code>id</code> is missing, print <code>** instance id missing **</code> (ex: <code>$ update BaseModel</code>)</li>
<li>If the instance of the class name doesn't exist for the <code>id</code>, print <code>** no instance found **</code>  (ex: <code>$ update BaseModel 121212</code>)</li>
<li>If the attribute name is missing, print <code>** attribute name missing **</code> (ex: <code>$ update BaseModel existing-id</code>)</li>
<li>If the value for the attribute name doesn't exist, print <code>** value missing **</code> (ex: <code>$ update BaseModel existing-id first_name</code>)</li>
<li>All other arguments should not be used (Ex: <code>$ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com" first_name "Betty"</code> = <code>$ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"</code>)</li>
</ul></li>
</ul><p>Let's add some rules:</p><ul>
<li>You can assume arguments are always in the right order</li>
<li>Each arguments are separated by a space</li>
<li>A string argument with a space must be between double quote</li>
<li>The error management starts from the first argument to the last one<br/></li>
</ul>


<h4 class="task">
    8. First User
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a class <code>User</code> that inherits from <code>BaseModel</code>:</p><ul>
<li><code>models/user.py</code></li>
<li>Public class attributes:

<ul>
<li><code>email</code>: string - empty string</li>
<li><code>password</code>: string - empty string</li>
<li><code>first_name</code>: string - empty string</li>
<li><code>last_name</code>: string - empty string</li>
</ul></li>
</ul><p>Update <code>FileStorage</code> to manage correctly serialization and deserialization of <code>User</code>.</p><p>Update your command interpreter (<code>console.py</code>) to allow <code>show</code>, <code>create</code>, <code>destroy</code>, <code>update</code> and <code>all</code> used with <code>User</code>.</p>


<h4 class="task">
    9. More classes!
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write all those classes that inherit from <code>BaseModel</code>:</p><ul>
<li><code>State</code> (<code>models/state.py</code>):

<ul>
<li>Public class attributes:

<ul>
<li><code>name</code>: string - empty string</li>
</ul></li>
</ul></li>
<li><code>City</code> (<code>models/city.py</code>):

<ul>
<li>Public class attributes:

<ul>
<li><code>state_id</code>: string - empty string: it will be the <code>State.id</code></li>
<li><code>name</code>: string - empty string</li>
</ul></li>
</ul></li>
<li><code>Amenity</code> (<code>models/amenity.py</code>):

<ul>
<li>Public class attributes:

<ul>
<li><code>name</code>: string - empty string</li>
</ul></li>
</ul></li>
<li><code>Place</code> (<code>models/place.py</code>):

<ul>
<li>Public class attributes:

<ul>
<li><code>city_id</code>: string - empty string: it will be the <code>City.id</code></li>
<li><code>user_id</code>: string - empty string: it will be the <code>User.id</code></li>
<li><code>name</code>: string - empty string</li>
<li><code>description</code>: string - empty string</li>
<li><code>number_rooms</code>: integer - 0</li>
<li><code>number_bathrooms</code>: integer - 0</li>
<li><code>max_guest</code>: integer - 0</li>
<li><code>price_by_night</code>: integer - 0</li>
<li><code>latitude</code>: float - 0.0</li>
<li><code>longitude</code>: float - 0.0</li>
<li><code>amenity_ids</code>: list of string - empty list: it will be the list of <code>Amenity.id</code> later</li>
</ul></li>
</ul></li>
<li><code>Review</code> (<code>models/review.py</code>):

<ul>
<li>Public class attributes:

<ul>
<li><code>place_id</code>: string - empty string: it will be the <code>Place.id</code></li>
<li><code>user_id</code>: string - empty string: it will be the <code>User.id</code></li>
<li><code>text</code>: string - empty string</li>
</ul></li>
</ul></li>
</ul>


<h4 class="task">
    10. Console 1.0
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Update <code>FileStorage</code> to manage correctly serialization and deserialization of all our new classes: <code>Place</code>, <code>State</code>, <code>City</code>, <code>Amenity</code> and <code>Review</code></p><p>Update your command interpreter (<code>console.py</code>) to allow those actions: <code>show</code>, <code>create</code>, <code>destroy</code>, <code>update</code> and <code>all</code> with all classes created previously.</p><p>Enjoy your first console!</p><p><strong>No unittests needed for the console</strong></p>


<h4 class="task">
    11. All instances by class name
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Update your command interpreter (<code>console.py</code>) to retrieve all instances of a class by using: <code>&lt;class name&gt;.all()</code>.</p>


<h4 class="task">
    12. Count instances
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Update your command interpreter (<code>console.py</code>) to retrieve the number of instances of a class: <code>&lt;class name&gt;.count()</code>.</p>


<h4 class="task">
    13. Show
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Update your command interpreter (<code>console.py</code>) to retrieve the an instances based on his ID: <code>&lt;class name&gt;.show(&lt;id&gt;)</code>.</p><p>Errors management must be the same as previously.</p>


<h4 class="task">
    14. Destroy
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Update your command interpreter (<code>console.py</code>) to destroy an instance based on his ID: <code>&lt;class name&gt;.destroy(&lt;id&gt;)</code>.</p><p>Errors management must be the same as previously.</p>


<h4 class="task">
    15. Update
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Update your command interpreter (<code>console.py</code>) to update an instance based on his ID: <code>&lt;class name&gt;.update(&lt;id&gt;, &lt;attribute name&gt;, &lt;attribute value&gt;)</code>.</p><p>Errors management must be the same as previously.</p>


<h4 class="task">
    16. Update from dictionary
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Update your command interpreter (<code>console.py</code>) to update an instance based on his ID with a dictionary: <code>&lt;class name&gt;.update(&lt;id&gt;, &lt;dictionary representation&gt;)</code>.</p><p>Errors management must be the same as previously.</p>


<h4 class="task">
    17. Unittests for the Console!
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Write all unittests for <code>console.py</code>, all features!</p>

