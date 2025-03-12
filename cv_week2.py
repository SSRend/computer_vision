import cv2

def main():
    # 사용 가능한 카메라 인덱스 찾기
    cap = None
    for i in range(5):  # 보통 0~4 사이에 웹캠이 존재함
        temp_cap = cv2.VideoCapture(i)
        if temp_cap.isOpened():
            cap = temp_cap
            print(f"웹캠 {i}를 사용합니다.")
            break
        temp_cap.release()
    
    if cap is None:
        print("사용 가능한 웹캠이 없습니다.")
        return
    
    # 동영상 저장 설정
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))
    
    recording = False  # 녹화 상태 변수
    mirror = False  # 좌우반전 상태 변수
    
    while True:
        # 프레임 읽기
        ret, frame = cap.read()
        if not ret:
            print("프레임을 읽을 수 없습니다.")
            break
        
        # 좌우 반전 적용
        if mirror:
            frame = cv2.flip(frame, 1)
        
        # 녹화 중이면 영상 저장 및 표시
        if recording:
            out.write(frame)
            cv2.circle(frame, (50, 50), 10, (0, 0, 255), -1)  # 빨간색 원 표시
        
        # 화면에 프레임 출력
        cv2.imshow('Webcam', frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC 키로 종료
            break
        elif key == 32:  # Space 키로 녹화 상태 변경
            recording = not recording
            print("녹화 시작" if recording else "녹화 중지")
        elif key == ord('m'):  # 'M' 키로 좌우 반전 토글
            mirror = not mirror
            print("좌우 반전 적용" if mirror else "좌우 반전 해제")
    
    # 자원 해제
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()