# Nathan Stevenson

import urllib.request
import re

specified_department = input("Specify a department: ")
specified_class_number = input("Specify a class number: ")
specific_teacher = input("Would you like to specify a teacher? If not press Enter: ")

class_pattern = r"""<h3 id="title">([A-Z][a-z]* [A-Z][a-z]*)</h3>
                
            </div>
        </a>
      <div class="col-md-8">
        <div class="card-body">
          <div class="row justify-content-between text-center text-md-left">
              <div class="col-4 col-lg-2 text-nowrap">
                <small class="mb-0 text-uppercase">
                  <i class="fa fa-star fa-fw"></i>&nbsp;Rating
                </small>
                <p class="mb-0 info" id="rating">
                  
                    ([0-9].[0-9][0-9])
                  
                </p>
              </div> 
              <div class="col-4 col-lg-2 text-nowrap">
                <small class="mb-0 text-uppercase">
                  <i class="fa fa-dumbbell fa-fw"></i>&nbsp;Difficulty
                </small>
                <p class="mb-0 info" id="difficulty">
                  
                    ([0-9].[0-9][0-9])
                  
                </p>
              </div>
              <div class="col-4 col-lg-2 text-nowrap">
                <small class="mb-0 text-uppercase">
                  <i class="fas fa-chart-bar"></i>&nbsp;GPA
                </small>
                <p class="mb-0 info" id="gpa">
                  
                    ([0-9].[0-9][0-9]|&mdash;)
                  
                </p>
              </div>"""
finder = re.compile(class_pattern)

# Set up for accessing theCourseForum for GPA and difficulty
specific_class = specified_department + "/" + specified_class_number
url = "https://thecourseforum.com/course/" + specific_class
raw_data = urllib.request.urlopen(url)
data = raw_data.read().decode("utf-8")


if specific_teacher != "":
    for match in finder.finditer(data):
        if specific_teacher == match.group(1):
            print()
            print(match.group(1).replace("&mdash;", "No Data") + "\n" +
                  "Rating: " + match.group(2).replace("&mdash;", "No Data") + "\n" +
                  "Difficulty: " + match.group(3).replace("&mdash;", "No Data") + "\n" +
                  "Average GPA: " + match.group(4).replace("&mdash;", "No Data") + "\n" +
                  "----------------------------------")

elif specific_teacher == "":
    for match in finder.finditer(data):
        print()
        print(match.group(1).replace("&mdash;", "No Data") + "\n" +
              "Rating: " + match.group(2).replace("&mdash;", "No Data") + "\n" +
              "Difficulty: " + match.group(3).replace("&mdash;", "No Data") + "\n" +
              "Average GPA: " + match.group(4).replace("&mdash;", "No Data") + "\n" +
              "----------------------------------")
