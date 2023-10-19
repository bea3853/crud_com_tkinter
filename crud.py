import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicativo de Agenda de Contatos")
        
        self.contacts = []
        
        self.create_gui()
        
    def create_gui(self):
        self.name_label = tk.Label(self.root, text="Nome:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()
        
        self.email_label = tk.Label(self.root, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack()
        
        self.phone_label = tk.Label(self.root, text="Telefone:")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.pack()
        
        self.add_button = tk.Button(self.root, text="Adicionar Contato", command=self.add_contact)
        self.add_button.pack()
        
        self.contacts_listbox = tk.Listbox(self.root, width=40, height=10)
        self.contacts_listbox.pack()
        
        self.view_button = tk.Button(self.root, text="Visualizar Contato", command=self.view_contact)
        self.view_button.pack()
        
        self.update_button = tk.Button(self.root, text="Atualizar Contato", command=self.update_contact)
        self.update_button.pack()
        
        self.delete_button = tk.Button(self.root, text="Excluir Contato", command=self.delete_contact)
        self.delete_button.pack()
        
        self.load_contacts()
        
    def add_contact(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        
        if name and email and phone:
            contact = Contact(name, email, phone)
            self.contacts.append(contact)
            self.contacts_listbox.insert(tk.END, name)
            self.clear_entries()
            self.save_contacts()
        else:
            messagebox.showwarning("Campos Vazios", "Preencha todos os campos.")
    
    def view_contact(self):
        selected_index = self.contacts_listbox.curselection()
        
        if selected_index:
            contact = self.contacts[selected_index[0]]
            messagebox.showinfo("Detalhes do Contato", f"Nome: {contact.name}\nEmail: {contact.email}\nTelefone: {contact.phone}")
        else:
            messagebox.showwarning("Nenhum Contato Selecionado", "Selecione um contato na lista.")
    
    def update_contact(self):
        selected_index = self.contacts_listbox.curselection()
        
        if selected_index:
            name = self.name_entry.get()
            email = self.email_entry.get()
            phone = self.phone_entry.get()
            
            if name and email and phone:
                contact = self.contacts[selected_index[0]]
                contact.name = name
                contact.email = email
                contact.phone = phone
                self.save_contacts()
                self.load_contacts()
                self.clear_entries()
            else:
                messagebox.showwarning("Campos Vazios", "Preencha todos os campos.")
        else:
            messagebox.showwarning("Nenhum Contato Selecionado", "Selecione um contato na lista.")
    
    def delete_contact(self):
        selected_index = self.contacts_listbox.curselection()
        
        if selected_index:
            confirmation = messagebox.askyesno("Excluir Contato", "Tem certeza que deseja excluir o contato selecionado?")
            
            if confirmation:
                del self.contacts[selected_index[0]]
                self.contacts_listbox.delete(selected_index[0])
                self.clear_entries()
                self.save_contacts()
        else:
            messagebox.showwarning("Nenhum Contato Selecionado", "Selecione um contato na lista.")
    
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
    
    def save_contacts(self):
        with open("contacts.txt", "w") as file:
            for contact in self.contacts:
                file.write(f"{contact.name},{contact.email},{contact.phone}\n")
    
    def load_contacts(self):
        self.contacts_listbox.delete(0, tk.END)
        self.contacts.clear()
        try:
            with open("contacts.txt", "r") as file:
                for line in file:
                    name, email, phone = line.strip().split(',')
                    contact = Contact(name, email, phone)
                    self.contacts.append(contact)
                    self.contacts_listbox.insert(tk.END, name)
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
