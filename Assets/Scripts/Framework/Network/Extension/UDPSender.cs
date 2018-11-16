
using UnityEngine;
using System.Collections;

using System;
using System.Text;
using System.Net;
using System.Net.Sockets;
using System.Threading;

public class UDPSender : MonoBehaviour
{
    public static UDPSender _Instance;

    public int remotePort = 7009;  //Զ�˶˿ں�
    public string remoteIpStr = "127.0.0.1"; //

    UdpClient client = null;

    IPAddress remoteIP;
    IPEndPoint remotePoint;

    void Awake()
    {
        _Instance = this;
    }

    void Start()
    {
        Console.WriteLine("��ʼ��");

        client = new UdpClient();
    }

    public void Send(byte[] data)
    {
        remoteIP = IPAddress.Parse(remoteIpStr);
        remotePoint = new IPEndPoint(remoteIP, remotePort);//ʵ����һ��Զ�̶˵� 
        client.Send(data, data.Length, remotePoint);//�����ݷ��͵�Զ�̶˵� 
    }

    void OnApplicationQuit()
    {
        client.Close();
    }

}