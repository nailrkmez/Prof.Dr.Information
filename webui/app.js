document.addEventListener('DOMContentLoaded', () => {
    const chatForm = document.getElementById('chatForm');
    const userInput = document.getElementById('userInput');
    const messagesContainer = document.getElementById('messagesContainer');
    const navBtns = document.querySelectorAll('.nav-btn');
    const attachBtn = document.getElementById('attachBtn');
    const imageInput = document.getElementById('imageInput');
    const imagePreviewContainer = document.getElementById('imagePreviewContainer');
    const imagePreview = document.getElementById('imagePreview');
    const removeImgBtn = document.getElementById('removeImgBtn');
    const uploadDocBtn = document.getElementById('uploadDocBtn');
    const fileDocInput = document.getElementById('fileDocInput');
    const clearMemBtn = document.getElementById('clearMemBtn');
    const memCount = document.getElementById('memCount');

    let currentImageBase64 = null;

    // Geçmiş hafıza sayısını ve sohbeti yükle
    async function loadHistory() {
        try {
            const res = await fetch('/api/history');
            const data = await res.json();
            if (data.history && data.history.length > 0) {
                memCount.innerText = `Hafıza: ${data.history.length} Tur Kayıtlı`;
                // Geçmiş mesajları ekrana dök
                data.history.forEach(item => {
                    appendMessage('user', 'Klinisyen', item.user);
                    appendMessage('assistant', 'Prof. Dr. Information', item.assistant);
                });
            } else {
                memCount.innerText = 'Hafıza: Temiz';
            }
        } catch (e) {
            memCount.innerText = 'Hafıza: Aktif';
        }
    }
    loadHistory();

    // Hafızayı Temizle
    clearMemBtn.addEventListener('click', async () => {
        if (confirm('Geçmiş klinik sohbet hafızasını sıfırlamak istiyor musunuz?')) {
            try {
                await fetch('/api/clear_history', { method: 'POST' });
                messagesContainer.innerHTML = '';
                appendMessage('assistant', 'Prof. Dr. Information', 'Klinik sohbet hafızası sıfırlandı. Yeni vaka incelemesine hazırım.');
                memCount.innerText = 'Hafıza: Temiz';
            } catch (err) {
                alert('Hafıza temizlenirken hata oluştu.');
            }
        }
    });

    // Görsel Ekleme
    attachBtn.addEventListener('click', () => imageInput.click());

    imageInput.addEventListener('change', (e) => {
        const file = e.target.files[0];
        if (!file) return;

        const reader = new FileReader();
        reader.onload = (event) => {
            currentImageBase64 = event.target.result;
            imagePreview.src = currentImageBase64;
            imagePreviewContainer.style.display = 'flex';
        };
        reader.readAsDataURL(file);
    });

    removeImgBtn.addEventListener('click', () => {
        currentImageBase64 = null;
        imageInput.value = '';
        imagePreviewContainer.style.display = 'none';
    });

    // Belge Yükleyerek Modeli Sürekli Eğitme / Hafızasına Katma
    uploadDocBtn.addEventListener('click', () => fileDocInput.click());

    fileDocInput.addEventListener('change', async (e) => {
        const file = e.target.files[0];
        if (!file) return;

        const reader = new FileReader();
        reader.onload = async (event) => {
            const content = event.target.result;
            try {
                const res = await fetch('/api/learn', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        topic: file.name,
                        content: content
                    })
                });
                const data = await res.json();
                alert(`✅ [Başarılı] "${file.name}" belgesi klinik bilgi hazinesine eklendi ve modelin kalıcı belleğine işlendi.`);
            } catch (err) {
                alert('Belge işlenirken hata oluştu.');
            }
        };
        reader.readAsText(file);
    });

    // Klinik Protokol Butonları
    navBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            navBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            userInput.value = btn.getAttribute('data-prompt');
            userInput.focus();
        });
    });

    // Enter ile gönder
    userInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            chatForm.dispatchEvent(new Event('submit'));
        }
    });

    // Mesaj Gönderme
    chatForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const text = userInput.value.trim();
        if (!text && !currentImageBase64) return;

        const imageToSend = currentImageBase64;
        appendMessage('user', 'Klinisyen', text, imageToSend);

        userInput.value = '';
        currentImageBase64 = null;
        imageInput.value = '';
        imagePreviewContainer.style.display = 'none';

        const loadingId = appendMessage('assistant', 'Prof. Dr. Information', 'Klinik vaka ve multimodal parametreler analiz ediliyor...');

        try {
            const res = await fetch('/api/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    message: text,
                    image: imageToSend
                })
            });

            const data = await res.json();
            const reply = data.response || data.error || 'Yanıt alınamadı.';

            const loadingBubble = document.getElementById(loadingId);
            if (loadingBubble) {
                loadingBubble.querySelector('.content').innerHTML = formatMarkdown(reply);
            }
        } catch (err) {
            const loadingBubble = document.getElementById(loadingId);
            if (loadingBubble) {
                loadingBubble.querySelector('.content').innerText = 'Hata: ' + err.message;
            }
        }

        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    });

    function appendMessage(role, name, content, imgSrc = null) {
        const msgId = 'msg-' + Date.now() + Math.random().toString().slice(2, 6);
        const msgDiv = document.createElement('div');
        msgDiv.className = `message ${role}`;
        msgDiv.id = msgId;

        const avatar = role === 'user' ? '🩺' : '👨‍⚕️';
        let imgHtml = '';
        if (imgSrc) {
            imgHtml = `<img src="${imgSrc}" class="msg-img-preview" alt="Eklenen Tıbbi Görsel">`;
        }

        msgDiv.innerHTML = `
            <div class="avatar">${avatar}</div>
            <div class="bubble">
                <div class="sender-name">${name}</div>
                ${imgHtml}
                <div class="content">${formatMarkdown(content)}</div>
            </div>
        `;

        messagesContainer.appendChild(msgDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
        return msgId;
    }

    function formatMarkdown(text) {
        if (!text) return '';
        return text
            .replace(/<think>([\s\S]*?)<\/think>/g, '<div style="background:rgba(255,255,255,0.03); border-left: 3px solid #38bdf8; padding: 10px 14px; margin: 10px 0; border-radius: 6px; font-size:12.5px; color:#94a3b8;"><strong style="color:#38bdf8;">🧠 Klinik Muhakeme & Düşünce Zinciri:</strong><br>$1</div>')
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/### (.*?)\n/g, '<h3 style="color:#38bdf8; margin: 10px 0 6px 0;">$1</h3>')
            .replace(/\n\n/g, '<br><br>')
            .replace(/\n/g, '<br>');
    }
});
