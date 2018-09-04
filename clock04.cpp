#define hParentKey HKEY_CURRENT_USER
#define lpszSubKey "Software\\Kumei\\Clock"
#define PAI 3.14159

#define CLOCK_WIDTH 250        //時計全体のウィンドウ幅
#define CLOCK_HEIGHT 60        //高さ
#define MYTIMER 1            //タイマーID
#include <windows.h>
#include <math.h>

typedef struct MYDATA {
    COLORREF cr_bg;
    COLORREF cr_txt;
    int x;
    int y;
} INIDATA;

LRESULT CALLBACK WndProc(HWND, UINT, WPARAM, LPARAM);
ATOM InitApp(HINSTANCE);
BOOL InitInstance(HINSTANCE, int);
HFONT SetMyFont(LPCTSTR, int);
BOOL GetMyColor(HWND, COLORREF *, COLORREF);
void GetInitialSettings(INIDATA *);
BOOL GetDataDWORD(char *, DWORD *);
BOOL SetInitialSettings(INIDATA);
BOOL SetDataDWORD(char *, DWORD);
BOOL ShowClock(HDC, char *);
BOOL GetHMS(char *, int *, int *, int *);

char szClassName[] = "clock04";    //ウィンドウクラス
char szAppName[] = "猫クロック"; //アプリケーション名
HINSTANCE hInst;
