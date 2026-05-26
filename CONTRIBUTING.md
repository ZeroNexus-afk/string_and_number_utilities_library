# Hướng dẫn đóng góp (Contributing Guidelines) 

Cảm ơn bạn đã quan tâm và muốn đóng góp cho dự án **String and Number Utilities Library**! Dưới đây là các bước quy chuẩn để bạn gửi code của mình vào dự án một cách chuyên nghiệp nhất.

## Quy trình đóng góp (Workflow)

1. **Fork dự án:** Nhấn nút `Fork` ở góc trên bên phải kho chứa này để tạo một bản sao về tài khoản GitHub cá nhân của bạn.
2. **Clone về máy:** Tải bản sao đó về máy tính (`git clone ...`).
3. **Tạo nhánh làm việc:** Tạo nhánh riêng cho tính năng bạn muốn làm. Tên nhánh phải rõ ràng.
   `git checkout -b feature-ten-tinh-nang`
4. **Viết Code và Unit Test:**
   - Code chính phải đặt trong thư mục `src/`.
   - BẮT BUỘC phải viết Unit Test tương ứng trong thư mục `tests/`.
   - Đảm bảo tất cả các test đều Pass trước khi đẩy code. 
5. **Commit và Push:**
   - Ghi chú commit rõ ràng mục đích thay đổi.
   - Push nhánh đó lên kho Fork của bạn.
6. **Tạo Pull Request (PR):**
   - Lên GitHub, tạo Pull Request từ nhánh của bạn vào nhánh `main` của dự án gốc.
   - Nhớ đính kèm thẻ `Closes #số_issue` nếu có Issue liên quan.

## Yêu cầu Code Review
- Maintainer sẽ là người trực tiếp đọc code và kiểm tra dấu tick xanh của GitHub Actions (CI/CD).
- Nếu bị Request changes, vui lòng sửa lại code và push thẳng lên nhánh cũ.
- Chỉ Maintainer mới có quyền bấm Merge gộp code.
