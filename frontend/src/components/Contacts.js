import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './Contacts.css';
import ContactDetail from './ContactDetail';

const Contacts = () => {
  const [contacts, setContacts] = useState([]);
  const [selectedContact, setSelectedContact] = useState(null);
  const [modalIsOpen, setModalIsOpen] = useState(false);

  useEffect(() => {
    const fetchContacts = async () => {
      try {
        const response = await axios.get('https://contacts-app-qsy5.onrender.com/contacts/get_contacts', {
          headers: {
            'Content-Type': 'application/json',
          },
        });
        setContacts(response.data);
      } catch (error) {
        console.error("There was an error fetching the contacts!", error);
      }
    };

    fetchContacts();
  }, []);

  const openModal = (contact) => {
    setSelectedContact(contact);
    setModalIsOpen(true);
  };

  const closeModal = () => {
    setSelectedContact(null);
    setModalIsOpen(false);
  };

  return (
    <div className="contacts-container">
      <h1>My Contacts</h1>
      <ul className="contacts-list">
        {contacts.map(contact => (
          <li key={contact.id} className="contact-item" onClick={() => openModal(contact)}>
            <span className="contact-name">{contact.name}</span>
            <span className="contact-email">{contact.email}</span>
          </li>
        ))}
      </ul>
      <ContactDetail
        isOpen={modalIsOpen}
        onRequestClose={closeModal}
        contact={selectedContact}
      />
    </div>
  );
};

export default Contacts;
