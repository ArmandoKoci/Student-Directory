students = []
file = open("students.txt","a")
file.close()

def show_main_Menu():
    print("\n ---Κεντρικό Μενού--- ")
    print("1. Προβολή όλων των φοιτητών.\n2. Αναζήτηση φοιτητών.\n3. Εισαγωγή νέου φοιτητή.\n4. Διαγραφή φοιτητή.\n5. Εκτύπωση λίστας φοιτητών.\n6. Έξοδος από την εφαρμογή.")


#1.Προβολή όλων των φοιτητών!!!
def print_students(students):
        print("Λίστα Φοιτητών:")
        print("A/A\tΕΠΙΘΕΤΟ\tΟΝΟΜΑ\tΤΗΛΕΦΩΝΟ\tΑ.Μ.")
        for i, student in enumerate(students,start=1): #παρακαλουθει τον αριθμό των επαναλήψεων σε έναν βρόχο.
            print(f"{i}.\t{student['Επίθετο']}\t{student['Όνομα']}\t{student['Τηλέφωνο']}\t{student['Αριθμός Μητρώου']}")



#2.Αναζήτηση φοιτητών!!!
def search_student(students):
        print("Αναζήτηση Φοιτητή")
        print("Επέλεξε πεδίο αναζήτησης: ")
        print("1.Επίθετο")
        print("2.Όνομα")
        print("3.Τηλέφωνο")
        print("4.Αριθμός Μητρώου")

        choice = input("Επιλέξτε μια απο τις λειτουργίες (1-4): ")

        if choice not in {"1","2","3","4"}:
            print("Μη Έγκυρη επιλογή")
            return
        
        search_field = input("Εισάγετε τι επιθυμείτε να περιέχει το πεδίο: ")  

        results = []

        for student in students:
            #ελεγχος εαν το search_field που επελεξε ο χρηστης να δωσει υπαρχει σε καποιον φοιτητη απο την λιστα μας.
            if search_field.lower() in student[list(student.keys())[int(choice)-1]].lower():
                results.append(student)

        print_students(results)



#3.Εισαγωγή νέου φοιτητή!!!
def add_student(students):
    while True:
        print("Εισαγωγή νέου φοιτητή")

        Επίθετο = input("Επίθετο : ")
        Όνομα = input("Όνομα : ")
        Τηλέφωνο = input("Τηλέφωνο : ")
        Αριθμός_Μητρώου = input("Αριθμός Μητρώου : ")

        if not Επίθετο.isalpha() or not Όνομα.isalpha():
            print("Λάθος.Το επίθετο και το όνομα πρεπει να μην περιεχουν αριθμους αλλα μόνο γράμματα")
            continue
        if len(Επίθετο) > 15 or len(Όνομα) > 15:
            print("Λάθος.Το επίθετο και το όνομα δεν πρέπει να ξεπερνούν σε μήκος τα 15 χαρακτηριστικά ")
            continue
        if not Τηλέφωνο.isdigit() or len(Τηλέφωνο) != 10:
            print("Λάθος.Το τηλέφωνο πρέπει να αποτελείται απο 10 ψηφία και οχι χαρακτήρες")
            continue
        if not Αριθμός_Μητρώου.isdigit():
            print("Λάθος.Ο αριθμός μητρώου δεν πρέπει να περιέχει χαρακτήρες")
            continue

        break #εαν ολες οι προϋποθέσεις ικανοποιούνται τοτε βγαινουμε απο την επανάληψη.
       

    #εχουμε κλειδια τις λεξεις επιθετο,ονομα,τηλεφωνο,αμ τα οποια ειναι χαρακτηριστικα του φοιτητη 
    #το new_student (dictionary) προστιθεται στη λιστα students με το append (συναρτηση)
    new_student = {
        'Επίθετο' : Επίθετο,
        'Όνομα' : Όνομα,
        'Τηλέφωνο' : Τηλέφωνο,
        'Αριθμός Μητρώου' : Αριθμός_Μητρώου
    } 
    students.append(new_student)
    print("Επιτυχής εισαγώγη φοιτήτη")

    file = open("students.txt","a")

    file.write( Επίθετο )
    file.write(" ")
    file.write( Όνομα )
    file.write(" ") 
    file.write( Τηλέφωνο )
    file.write(" ")
    file.write( Αριθμός_Μητρώου )
    file.write("\n")

    file.close()


#4.Διαγραφή φοιτητή!!!
def delete_students(students):
        print_students(students)

        if not students:
            print("Δεν υπάρχουν φοιτητές για διαγραφή.")
            return

        student_index = input("Επιλέξτε τον Α/Α του φοιτητή που θέλετε να διαγράψετε: ")
        #ελέγχει εαν το Α/Α του φοιτητή ειναι ψηφία ,εαν είναι εκτος του ευρους 1 μεχρι και τον συνολικο αριθμό των φοιτητών στη λιστα 
        #εαν ειναι αληθής τοτε ειναι μη εγκυρος
        if not student_index.isdigit() or int(student_index) < 1 or int(student_index) > len(students):
             print("Μη έγκυρος Α/Α.")
             return
        
    #Διαγραφή του φοιτητη απο τη λιστα 
      
     # .pop - το στοιχειο που βρισκεται στην θεση που υπολογίστηκε στο προηγούμενο βήμα αφαιρείται απο τη λίστα students
     # το αφαιρεθέν στοιχειο αποθηκεύεται στην μεταβλητη deleted_student.
     # μετατροπή του student_index σε ακέραιο και αφαιρώ 1 για να προσαρμοστεί ο αριθμός μητρώου που δίνει ο χρήστης
     # στον δείκτη λίστας, πχ εαν εισάγει το 1, τότε ο αντίστοιχος δείκτης είναι το 0.

        deleted_student = students.pop(int(student_index)-1)
        print(f"Επιτυχής διαγραφή του φοιτητή: {deleted_student['Επίθετο']} {deleted_student['Όνομα']}")



#5.Εκτύπωση λίστας φοιτητών!!!
def print_to_file():
    file = open("students.txt","r")
    for x in file:
            print(x)
    file.close()
    

def main():
    while True:
        show_main_Menu()

        choice = input("Επελεξε μια απο τις επιλογες (1-6): ")

        if choice == "1":
            print_students(students)

        elif choice == "2":
            search_student(students)

        elif choice == "3":
            add_student(students)

        elif choice == "4":
            delete_students(students)
    
        elif choice == "5":
            print_to_file()

        elif choice == "6":
            print("Έξοδος από την εφαρμογή.")
            break
        else:
            print("Μη έγκυρη επιλογή. Παρακαλώ εισάγετε έναν έγκυρο αριθμό απο το 1 εως το 6.")
main()

